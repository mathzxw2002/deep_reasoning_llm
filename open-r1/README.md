
# step 1 : run openr1 container, using host directory "/root/deepr1" as a volume "voldsr1", and increasing shm size to 16g. test is the docker image name.

nvidia-docker run -it -v /root/deepr1:/voldsr1 --shm-size=16g test1

# step 2: install open-r1 and train deepseek r1 model

https://github.com/huggingface/open-r1


#revise dependencies to the corresponding version and install open-r1 by 

pip install -e ".[dev]"

![img_v3_02l6_60f6141e-290a-443c-9997-6e141122db4m](https://github.com/user-attachments/assets/15d4baff-9eb2-402f-991f-306c75493eba)


# step 3 

ACCELERATE_LOG_LEVEL=info accelerate launch --config_file recipes/accelerate_configs/zero2.yaml  src/open_r1/grpo.py     --config recipes/DeepSeek-R1-Distill-Qwen-1.5B/grpo/config_demo.yaml --fp16 True
