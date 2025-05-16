import argparse
import os
import sys
import json

from constraint_registry import INSTRUCTION_DICT

parser = argparse.ArgumentParser()
parser.add_argument('--hypothesis_path', type=str)
parser.add_argument('--data_path', type=str)
parser.add_argument("--delimiter", type=str, default = "</think>")
args = parser.parse_args()


def test_instruction_following_strict(
    instruction_id_list,
    response,
    parameters,
    prompt,
):
    """Tests response to see if instructions are followed."""

    is_following_list = []
    for index, instruction_id in enumerate(instruction_id_list):
        try:
            instruction_cls = INSTRUCTION_DICT[instruction_id]
        except:
            import pdb
            pdb.set_trace()
        instruction = instruction_cls(instruction_id)

        # Remove None values from kwargs to avoid unexpected keyword argument errors in build_description method.  
        if parameters[index]:
            kwargs = {n: p for n, p in parameters[index].items() if p}
        else:
            kwargs = {}
        instruction.build_description(**kwargs)
        args = instruction.get_constraint_args()
        if args and "prompt" in args:
            instruction.build_description(prompt=prompt)
        try:
            if response.strip() and instruction.check_following(response):
                is_following_list.append(True)
            else:
                is_following_list.append(False)
        except:
            import pdb
            pdb.set_trace()

    return is_following_list


strict = []
loose = []



for line1,line2 in zip(open(args.hypothesis_path).readlines(), open(args.data_path).readlines()):
    try:
        hypothesis = json.loads(line1)["output"]
    except:
        hypothesis = json.loads(line1)["response"]
    if isinstance(hypothesis,list):
        hypothesis = hypothesis[0]
    has_end_think = '</think>' in hypothesis
    has_start_think = '<think>' in hypothesis

    think = hypothesis
    if has_end_think:
        think = think.split("</think>")[0]
    if '<think>' in think:
        think = think.split('<think>')[1]
    
    if '<think>' in hypothesis:
        hypothesis = hypothesis.split('<think>')[1]
    if '</think>' in hypothesis:
        hypothesis = hypothesis.split('</think>')[1]
    if '<answer>' in hypothesis:
        hypothesis = hypothesis.split('<answer>')[1]
    if '</answer>' in hypothesis:
        hypothesis = hypothesis.split('</answer>')[0] 

    
    data = json.loads(line2)
    if not ("noconstraint" in args.hypothesis_path):
        is_follow_list = test_instruction_following_strict(
            data["constraint_name"],
            hypothesis,
            data["constraint_args"],
            data["question"],
        )
        strict.append(all(is_follow_list))
        loose.append(sum(is_follow_list)/len(is_follow_list))
    else:
        # only place holder
        strict.append(1)
        loose.append(1)



print(sum(strict)/len(strict))
print(sum(loose)/len(loose))