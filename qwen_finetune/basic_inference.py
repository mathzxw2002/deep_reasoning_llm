from vllm import LLM, SamplingParams

#https://github.com/vllm-project/vllm/issues/6723https://github.com/vllm-project/vllm/issues/6723


# Sample prompts.
prompts = [
    "You will be given a problem. Please reason step by step, and put your final answer within \boxed{} : .3. (6 points) A construction company was building a tunnel. When $\frac{1}{3}$ of the tunnel was completed at the original speed, they started using new equipment, which increased the construction speed by $20 \%$ and reduced the working hours to $80 \%$ of the original. As a result, it took a total of 185 days to complete the tunnel. If they had not used the new equipment and continued at the original speed, it would have taken $\qquad$ days to complete the tunnel.",
]

# Create an LLM.
llm =   LLM(model="/voldsr1/training_data/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-1___5B",
        dtype="half", tensor_parallel_size=4, gpu_memory_utilization=0.95, enable_chunked_prefill=False,
)

sampling_params = SamplingParams(
    temperature=0.8,
    top_p=0.9,
    max_tokens=2048,
)

# Generate texts from the prompts. The output is a list of RequestOutput objects
# that contain the prompt, generated text, and other information.
outputs = llm.generate(prompts, sampling_params)
# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
