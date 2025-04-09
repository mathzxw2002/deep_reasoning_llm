# install vllm
FROM  deepr1:vbase

ENV PATH "/root/miniconda3/bin:$PATH"

#
RUN conda install pip

#
COPY condarc root/.condarc
COPY xgrammar.zip root/
COPY xformers.zip root/
COPY vllm.zip root/
COPY requirements_xformers_torch2.5.txt root/xformers/
COPY requirements-common_vllm_xgrammar_higher.txt root/vllm/

#
RUN pip install pybind11[global] && \
    pip install torch==2.5.1 torchvision torchaudio && \
    cd /root && unzip -a xgrammar.zip && cd xgrammar && pip install -e . && \
    cd /root && unzip -a xformers.zip && cd xformers && \cp -rf requirements_xformers_torch2.5.txt requirements.txt && pip install -e . && \
    python -m xformers.info && \
    cd /root && unzip -a vllm.zip && cd vllm && python use_existing_torch.py && \
    \cp -rf requirements-common_vllm_xgrammar_higher.txt requirements-common.txt && \
    pip install -r requirements-build.txt && \
    pip install -r requirements-common.txt && \
    pip install -e . --no-build-isolation  && \
    pip install deepspeed && \
    pip install accelerate && \
    pip install datasets && \
    pip install trl
