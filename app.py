import streamlit as st
import pymupdf4llm
from llama_cpp import Llama
import re
import tempfile
import time

# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(page_title="StudentAI", page_icon="🎓", layout="wide")

# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "sections" not in st.session_state:
    st.session_state.sections = []

# -----------------------------
# Load TinyLlama
# -----------------------------


@st.cache_resource
def load_model():
    return Llama(
        model_path="models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
        n_ctx=4096,
        n_threads=8,
        verbose=False,
    )


llm = load_model()

# -----------------------------
# Section Builder
# -----------------------------


def build_sections(markdown_text):
    sections = []

    parts = re.split(r"\n##\s+", markdown_text)

    for part in parts:
        part = part.strip()

        if not part:
            continue

        lines = part.split("\n", 1)

        title = lines[0]

        content = lines[1] if len(lines) > 1 else ""

        sections.append({"title": title, "content": content})

    return sections


# -----------------------------
# Retrieval
# -----------------------------


def retrieve(question, top_k=2):
    results = []

    query_words = question.lower().split()

    for section in st.session_state.sections:
        score = 0

        text = (section["title"] + " " + section["content"]).lower()

        for word in query_words:
            if word in text:
                score += 1

        results.append((score, section))

    results.sort(key=lambda x: x[0], reverse=True)

    return [item[1] for item in results[:top_k]]


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:
    st.title("📚 Upload PDF")

    uploaded_files = st.file_uploader(
        "Upload PDF Notes", type=["pdf"], accept_multiple_files=True
    )

    if st.button("Process PDFs"):
        if not uploaded_files:
            st.warning("Please upload at least one PDF.")

        else:
            all_sections = []

            with st.spinner("📖 Extracting PDF structure..."):
                for pdf in uploaded_files:
                    with tempfile.NamedTemporaryFile(
                        delete=False, suffix=".pdf"
                    ) as tmp:
                        tmp.write(pdf.read())

                        markdown_text = pymupdf4llm.to_markdown(tmp.name)

                    sections = build_sections(markdown_text)

                    all_sections.extend(sections)

            st.session_state.sections = all_sections

            st.success(f"Processed {len(uploaded_files)} PDF(s)")

            st.info(
                f"""
📄 Sections Created: {len(all_sections)}

⚡ Retrieval: Keyword Search

🤖 Model: TinyLlama

📚 Workflow: Mozilla Local Q&A
"""
            )

# -----------------------------
# Main UI
# -----------------------------

st.title("🎓 StudentAI")

st.caption("Mozilla-style Local Document Q&A")

# -----------------------------
# Chat History
# -----------------------------

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# User Question
# -----------------------------

question = st.chat_input("Ask a question from your PDFs...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.markdown(question)

    if not st.session_state.sections:
        answer = "Please upload and process PDF files first."

    else:
        retrieved_sections = retrieve(question, top_k=2)

        context = "\n\n".join([section["content"] for section in retrieved_sections])

        # Limit context size
        context = context[:1500]

        prompt = f"""
You are StudentAI.

Answer the question using ONLY the context.

Keep the answer under 4 sentences.

Do not repeat information.

If the answer is not found, say:

I could not find the answer in the document.

Context:
{context}

Question:
{question}

Answer:
"""

        with st.spinner("🤔 StudentAI is thinking..."):
            response = llm(prompt, max_tokens=120, temperature=0.2)

            answer = response["choices"][0]["text"].strip()

    with st.chat_message("assistant"):
        placeholder = st.empty()

        typed_text = ""

        for word in answer.split():
            typed_text += word + " "

            placeholder.markdown(typed_text)

            time.sleep(0.01)

        if st.session_state.sections:
            with st.expander("📄 Retrieved Context"):
                st.write(context)

    st.session_state.messages.append({"role": "assistant", "content": answer})
