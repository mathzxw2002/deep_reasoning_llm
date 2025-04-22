from transformers import AutoProcessor
from vllm import LLM, SamplingParams
#from qwen_vl_utils import process_vision_info

MODEL_PATH = "/root/.cache/modelscope/hub/models/Qwen/Qwen2.5-VL-32B-Instruct"

llm = LLM(
    model=MODEL_PATH,
    limit_mm_per_prompt={"image": 0, "video": 0}, dtype="half", tensor_parallel_size=8, enforce_eager=True, gpu_memory_utilization=0.95,
)

#"max_num_seqs": 256,
#"max_model_len": 8192,
#"enforce_eager": true
#https://docs.vllm.ai/en/latest/performance/optimization.html
#https://docs.vllm.ai/en/latest/serving/engine_args.html
#https://github.com/vllm-project/vllm/issues/6641
sampling_params = SamplingParams(
    temperature=0.8,
    top_p=0.9,
    repetition_penalty=1.05,
    max_tokens=2048,
    stop_token_ids=[],
)

image_messages = []

'''
    {"role": "system", "content": "You are a helpful assistant."},
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "https://modelscope.oss-cn-beijing.aliyuncs.com/resource/qwen.png",
                "min_pixels": 224 * 224,
                "max_pixels": 1280 * 28 * 28,
            },
            {"type": "text", "text": "What is the text in the illustrate?"},
        ],
    },
]'''

# For video input, you can pass following values instead:
# "type": "video",
# "video": "<video URL>",
video_messages = []
'''
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": [
            {"type": "text", "text": "请用表格总结一下视频中的商品特点"},
            {
                "type": "video", 
                "video": "https://duguang-labelling.oss-cn-shanghai.aliyuncs.com/qiansun/video_ocr/videos/50221078283.mp4",
                "total_pixels": 20480 * 28 * 28, "min_pixels": 16 * 28 * 28
            }
        ]
    },
]'''

# Here we use video messages as a demonstration
#messages = video_messages

messages =  [
    {"role": "system", "content": "You will be given a problem. Please reason step by step, and put your final answer within \boxed{}."},
    {
        "role": "user",
        "content": [
#            {"type": "text", "text": "3. (6 points) A construction company was building a tunnel. When $\frac{1}{3}$ of the tunnel was completed at the original speed, they started using new equipment, which increased the construction speed by $20 \%$ and reduced the working hours to $80 \%$ of the original. As a result, it took a total of 185 days to complete the tunnel. If they had not used the new equipment and continued at the original speed, it would have taken $\qquad$ days to complete the tunnel."},
#            {"type":"text", "text":"18. (3 points) Li Shuang rides a bike at a speed of 320 meters per minute from location $A$ to location $B$. On the way, due to a bicycle malfunction, he pushes the bike and walks for 5 minutes to a place 1800 meters from $B$ to repair the bike. After 15 minutes, he continues towards $B$ at 1.5 times his original riding speed, and arrives at $B$ 17 minutes later than the expected time. What is Li Shuang's walking speed in meters per minute?"},
             {"type":"text", "text":"2. As shown in Figure 1, the side length of rhombus $A B C D$ is $a$, and $O$ is a point on the diagonal $A C$, with $O A=a, O B=$ $O C=O D=1$. Then $a$ equals ( ). (A) $\frac{\sqrt{5}+1}{2}$ (B) $\frac{\sqrt{5}-1}{2}$ (C) 1 (D) 2"},
        ],
    },
]

processor = AutoProcessor.from_pretrained(MODEL_PATH)
prompt = processor.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
#image_inputs, video_inputs, video_kwargs = process_vision_info(messages, return_video_kwargs=True)

mm_data = {}
#if image_inputs is not None:
#    mm_data["image"] = image_inputs
#if video_inputs is not None:
#    mm_data["video"] = video_inputs


llm_inputs = {
    "prompt": prompt,
    "multi_modal_data": mm_data,

    # FPS will be returned in video_kwargs
    #"mm_processor_kwargs": video_kwargs,
}

outputs = llm.generate([llm_inputs], sampling_params=sampling_params)
generated_text = outputs[0].outputs[0].text

print(generated_text)



