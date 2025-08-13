# install Ubuntu22.04
FROM nvidia/cuda:12.0.0-devel-ubuntu22.04

RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak && \
    sed -i.bak "s@http://.*archive.ubuntu.com@http://mirrors.aliyun.com@g" /etc/apt/sources.list && \
    sed -i "s@http://.*security.ubuntu.com@http://mirrors.aliyun.com@g" /etc/apt/sources.list && \
    apt update && \
    apt upgrade -y && \
    apt install -y cmake git pip wget ffmpeg libx11-dev libxrandr-dev libxi-dev libxinerama-dev libxcursor-dev libgl1-mesa-dev && \
    python3 -m pip install --upgrade pip && \
    git clone --depth 1 https://github.com/hiyouga/LLaMA-Factory.git && \ 
    cd LLaMA-Factory && \ 
    pip install -e ".[torch,metrics]" --no-build-isolation
