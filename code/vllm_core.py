import argparse
from datasets import load_dataset   
from transformers import AutoModelForCausalLM, AutoTokenizer
# from peft import PeftModel
import os
import torch
from vllm import LLM, SamplingParams
import json
import sys
from pathlib import Path 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model_name_or_path', type=str, default="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")
parser.add_argument('--tokenizer_name_or_path', type=str, default=None)
parser.add_argument("--test_file",type=str,default=None)
parser.add_argument("--temperature",type=float,default=1.0)
parser.add_argument("--top_p",type=float,default=0.95)
parser.add_argument("--max_token",type=int,default=16384)
parser.add_argument("--n_sample",type=int,default=1)
parser.add_argument("--seed",type=int,default=None)
parser.add_argument("--no_constraint",action="store_true")
args = parser.parse_args()





def vllm_inference(prompt):
    num_gpus = torch.cuda.device_count()
    llm = LLM(model = args.model_name_or_path, 
            tokenizer = args.tokenizer_name_or_path if args.tokenizer_name_or_path else args.model_name_or_path, 
            dtype='bfloat16',
            tensor_parallel_size = 4,#num_gpus,
            trust_remote_code=True,
            )
    print('>>>>>> model loaded')

    sampling_params = SamplingParams(temperature = args.temperature, top_p = args.top_p, max_tokens = args.max_token, seed = args.seed, n = args.n_sample)    
    outputs = llm.generate(prompt, sampling_params)
    sorted_outputs = sorted(outputs, key=lambda output: int(output.request_id))
    print('>>>>>> generation done')

    return sorted_outputs



ds = load_dataset('json' if 'json' in args.test_file else 'parquet', data_files=args.test_file, split='train')
tokenizer = AutoTokenizer.from_pretrained(args.tokenizer_name_or_path if args.tokenizer_name_or_path else args.model_name_or_path)
prompt = []
cot = "Let's think step by step and output the final answer within \\boxed{}."
for i in range(len(ds)):
    if 'question' in ds.column_names:
        prompt.append(tokenizer.apply_chat_template([{
            "role": "user",
            "content": ds[i]['question']+ cot + (" ".join(ds[i]["constraint_desc"]) if not args.no_constraint else ""),
        }],tokenize=False, add_generation_prompt=True))
    elif "prompt" in ds.column_names:
        prompt.append(tokenizer.apply_chat_template(ds[i]["prompt"], tokenize=False, add_generation_prompt=True))

print(">>>>>>>>>>>>>>>>>>>>>>>>")
print(prompt[0])
print(">>>>>>>>>>>>>>>>>>>>>>>>")



output_path = "output/{}_{}_t{}p{}max{}seed{}.jsonl".format(args.model_name_or_path.replace("/","_"), args.test_file.split('/')[-1].split('.')[0], args.temperature, args.top_p, args.max_token, args.seed)  
os.makedirs(os.path.dirname(output_path), exist_ok=True)
output_path = output_path.replace(".jsonl", "_noconstraint.jsonl") if args.no_constraint else output_path


output = vllm_inference(prompt)
fout = open(output_path,'w')
for i in range(len(prompt)):
    fout.write(json.dumps({"output": [ output[i].outputs[j].text for j in range(args.n_sample)]}, ensure_ascii=False)+'\n')
fout.close()

