
```python
# 下载项目
git clone https://github.com/tloen/alpaca-lora.git

# 安装依赖
pip install -r requirements.txt

# 转化模型
python src/transformers/models/llama/convert_llama_weights_to_hf.py \
    --input_dir ../model/ \
    --model_size 7B \
    --output_dir ../model/7B-hf
	
# 官方单卡训练模型
python finetune.py \
    --base_model '../model/7B-hf' \
    --data_path '../train.json' \
    --output_dir '../alpaca-lora-output'

# 单机多卡(4*A100)训练模型
WORLD_SIZE=4 CUDA_VISIBLE_DEVICES=0,1,2,3 torchrun --nproc_per_node=4 --master_port=3192 finetune.py \
    --base_model '../model/7B-hf' \
    --data_path '../train.json' \
    --output_dir '../alpaca-lora-output' \
    --batch_size 1024 \
    --micro_batch_size 128 \
	--num_epochs 3

# 推理
python generate.py \
    --load_8bit \
    --base_model '../model/7B-hf' \
    --lora_weights '../alpaca-lora-output'
```

