
# 1, Fine-tuning 

## 1.1, Unsloth
Train your own model with Unsloth, an open-source framework for LLM fine-tuning and reinforcement learning.

At Unsloth, our mission is to make AI as accurate and accessible as possible. Train, run, evaluate and save gpt-oss, Llama, DeepSeek, TTS, Qwen, Mistral, Gemma LLMs 2x faster with 70% less VRAM.

Our docs will guide you through running & training your own model locally.

https://docs.unsloth.ai/

https://github.com/unslothai/unsloth

<img width="3194" height="992" alt="image" src="https://github.com/user-attachments/assets/77cc39b1-ffa2-4560-b2bc-211107be2952" />

https://docs.unsloth.ai/new/gpt-oss-reinforcement-learning


## 1.2, MS-Swift

## 1.3, Llama Factory



# 2, Inference 

## 2.1, huggingface optimum
https://github.com/huggingface/optimum

🚀 Accelerate inference and training of 🤗 Transformers, Diffusers, TIMM and Sentence Transformers with easy to use hardware optimization tools

Optimum is an extension of Transformers 🤖 Diffusers 🧨 TIMM 🖼️ and Sentence-Transformers 🤗, providing a set of optimization tools and enabling maximum efficiency to train and run models on targeted hardware, while keeping things easy to use.


## 2.2, sglang
SGLang is a fast serving framework for large language models and vision language models.

https://github.com/sgl-project/sglang

<img width="2392" height="728" alt="image" src="https://github.com/user-attachments/assets/22c6a945-370d-4822-a1d9-56b2431b5832" />

<img width="1281" height="651" alt="image" src="https://github.com/user-attachments/assets/b70fa506-df78-407f-846e-cf9297dbf4a3" />

## 2.3, TensorRT-LLM
https://github.com/NVIDIA/TensorRT-LLM

TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and support state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT LLM also contains components to create Python and C++ runtimes that orchestrate the inference execution in performant way.

<img width="1298" height="551" alt="image" src="https://github.com/user-attachments/assets/d3f8034e-562e-4d35-98cd-70a49532a0ad" />


## 2.4, vllm
https://github.com/vllm-project/vllm

A high-throughput and memory-efficient inference and serving engine for LLMs

<img width="3000" height="856" alt="image" src="https://github.com/user-attachments/assets/55747f16-d07a-47ed-8ccd-43f07d1a4349" />

<img width="1292" height="1015" alt="image" src="https://github.com/user-attachments/assets/930f8167-a26b-40a8-85a7-c2d63f07b2a6" />



# 3, LLM Quantization

## 3.1, Survey
A Comprehensive Study on Quantization Techniques for Large Language Models


### LLM Quantization | GPTQ | QAT | AWQ | GGUF | GGML | PTQ
<img width="878" height="430" alt="image" src="https://github.com/user-attachments/assets/977f6bd6-58a3-49d4-9ac1-dc7a244463be" />


https://medium.com/@siddharth.vij10/llm-quantization-gptq-qat-awq-gguf-ggml-ptq-2e172cd1b3b5


## 3.2, bitsandbytes

https://github.com/bitsandbytes-foundation/bitsandbytes

Accessible large language models via k-bit quantization for PyTorch.

<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/194c1e7a-9428-4765-acd5-5543047e3579" />

bitsandbytes enables accessible large language models via k-bit quantization for PyTorch. We provide three main features for dramatically reducing memory consumption for inference and training:

8-bit optimizers uses block-wise quantization to maintain 32-bit performance at a small fraction of the memory cost.
LLM.int8() or 8-bit quantization enables large language model inference with only half the required memory and without any performance degradation. This method is based on vector-wise quantization to quantize most features to 8-bits and separately treating outliers with 16-bit matrix multiplication.
QLoRA or 4-bit quantization enables large language model training with several memory-saving techniques that don't compromise performance. This method quantizes a model to 4-bits and inserts a small set of trainable low-rank adaptation (LoRA) weights to allow training.
The library includes quantization primitives for 8-bit & 4-bit operations, through bitsandbytes.nn.Linear8bitLt and bitsandbytes.nn.Linear4bit and 8-bit optimizers through bitsandbytes.optim module.

<img width="1166" height="1223" alt="image" src="https://github.com/user-attachments/assets/d9cdb98f-619b-496e-9adb-3bc42f055c5b" />


## 3.3, huggingface optimum-quanto
A pytorch quantization backend for optimum

https://github.com/huggingface/optimum-quanto

<img width="1289" height="974" alt="image" src="https://github.com/user-attachments/assets/09e92133-d062-4f7a-b566-afb6efb2dcbd" />



## 3.4, RWKV: Reinventing RNNs for the Transformer Era
https://arxiv.org/pdf/2305.13048

https://github.com/RWKV/rwkv.cpp


<img width="846" height="1090" alt="image" src="https://github.com/user-attachments/assets/325f637e-91bd-4a7c-a91b-4d4e10edc037" />


## 3.5, Quantization formats

https://bentoml.com/llm/getting-started/llm-quantization

<img width="1224" height="755" alt="image" src="https://github.com/user-attachments/assets/45ab49d8-cce2-4c39-8c57-41b8913fda92" />


### AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration

<img width="2016" height="462" alt="image" src="https://github.com/user-attachments/assets/9601966e-0180-4388-bf2b-68d93b75d06e" />


https://github.com/mit-han-lab/llm-awq


## 3.6, GPTQModel
LLM model quantization (compression) toolkit with hw acceleration support for Nvidia CUDA, AMD ROCm, Intel XPU and Intel/AMD/Apple CPU via HF, vLLM, and SGLang.

https://github.com/ModelCloud/GPTQModel

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/ae6d9c87-595b-4d8e-89dd-072ace03a5e6" />

<img width="1279" height="1121" alt="image" src="https://github.com/user-attachments/assets/ff4256ff-d95c-45a7-b057-25d208d7c489" />




