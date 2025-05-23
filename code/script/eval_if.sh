model=deepseek-ai_DeepSeek-R1-Distill-Qwen-1.5B
for dataset in gsm8k math500 minerva olympiad aime
do
    for constraint in single double triple 
    do 
        echo ${model}_${dataset}_${constraint}
        python3 -u code/eval_if.py \
            --data_path data/${dataset}_${constraint}.jsonl \
            --hypothesis_path output/${model}_${dataset}_${constraint}_t1.0p0.95max16384seedNone.jsonl

        echo ${model}_${dataset}_${constraint}_noconstraint
        python3 -u code/eval_if.py \
            --data_path data/${dataset}_${constraint}.jsonl \
            --hypothesis_path output/${model}_${dataset}_${constraint}_t1.0p0.95max16384seedNone_noconstraint.jsonl
    done
done


