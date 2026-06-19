from llama_cpp import Llama

llm = Llama(
    model_path="models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=8,
    verbose=False,
)

response = llm("What is sales forecasting?", max_tokens=200, temperature=0.2)

print(response["choices"][0]["text"])
