# build docker image for vllm
docker build -t vllm:deepr1

# build vllm, xformers and xgrammar from source code
vllm: https://github.com/vllm-project/vllm

xformers: https://github.com/facebookresearch/xformers

xgrammar: https://github.com/mlc-ai/xgrammar
