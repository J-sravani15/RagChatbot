import json

from llama_cpp import Llama

# Load sections
with open("sections.json", encoding="utf-8") as f:
    sections = json.load(f)

# Load model
llm = Llama(
    model_path="models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=8,
    verbose=False,
)


def retrieve(question, top_k=3):
    results = []

    query_words = question.lower().split()

    for section in sections:
        score = 0

        text = (section["title"] + " " + section["content"]).lower()

        for word in query_words:
            if word in text:
                score += 1

        results.append((score, section))

    results.sort(key=lambda x: x[0], reverse=True)

    return [item[1] for item in results[:top_k]]


question = input("Ask Question: ")

retrieved_sections = retrieve(question)

context = "\n\n".join([section["content"] for section in retrieved_sections])

prompt = f"""
Answer ONLY from the provided context.

If the answer is not available,
say:

I could not find the answer in the document.

Context:
{context}

Question:
{question}

Answer:
"""

response = llm(prompt, max_tokens=300, temperature=0.2)

print("\n")
print("=" * 60)
print("ANSWER")
print("=" * 60)
print(response["choices"][0]["text"])
