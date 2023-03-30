
```python
# 下载项目
git clone https://github.com/tatsu-lab/stanford_alpaca.git

# 安装
# 安装方式一
pip install git+https://github.com/huggingface/transformers@0041be5b3d1b9a5e1443e1825d7d80f6dfadcdaa
# 安装方式二
git clone https://github.com/huggingface/transformers.git
cd transformers
git checkout 0041be5
pip install .

# 下载转化仓库
git clone https://github.com/huggingface/transformers.git

# 安装一个额外的库
python -m pip install accelerate

# 转化模型
python src/transformers/models/llama/convert_llama_weights_to_hf.py \
    --input_dir ../model/ \
    --model_size 7B \
    --output_dir ../model/7B-hf

# 训练模型
torchrun --nproc_per_node=4 --master_port=11223 train.py \
    --model_name_or_path ../model/7B-hf \
    --data_path ../train.json \
    --bf16 True \
    --output_dir ../stanford_alpaca_output \
    --num_train_epochs 3 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 8 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 2000 \
    --save_total_limit 1 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --fsdp "full_shard auto_wrap" \
    --fsdp_transformer_layer_cls_to_wrap 'LLaMADecoderLayer' \
    --tf32 True
```

1. [参考1：standford-alpaca微调记录](https://zhuanlan.zhihu.com/p/616119919)
2. [参考2：stanford_alpaca/issues](https://github.com/tatsu-lab/stanford_alpaca/issues)