import streamlit as st
import numpy as np
import time
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from langchain_ollama import OllamaLLM

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(page_title="StudentAI", page_icon="🎓", layout="wide")

# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if "embeddings" not in st.session_state:
    st.session_state.embeddings = None

# -----------------------------
# Models
# -----------------------------


@st.cache_resource
def load_embedding_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


@st.cache_resource
def load_llm():
    return OllamaLLM(model="llama3")


embedding_model = load_embedding_model()
llm = load_llm()

# -----------------------------
# PDF Processing
# -----------------------------


def extract_text_from_pdf(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# -----------------------------
# Chunking
# -----------------------------


def chunk_text(text, chunk_size=3000, overlap=300):

    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks


# -----------------------------
# Similarity Search
# -----------------------------


def retrieve(query, top_k=3):

    query_embedding = embedding_model.encode([query])[0]

    similarities = []

    for emb in st.session_state.embeddings:
        similarity = np.dot(query_embedding, emb) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(emb)
        )

        similarities.append(similarity)

    top_indices = np.argsort(similarities)[-top_k:][::-1]

    return [st.session_state.chunks[i] for i in top_indices]


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:
    st.title("📚 Upload Notes")

    uploaded_files = st.file_uploader(
        "Upload PDF Notes", type=["pdf"], accept_multiple_files=True
    )

    if st.button("Process PDFs"):
        if not uploaded_files:
            st.warning("Please upload at least one PDF.")

        else:
            with st.spinner("📖 Reading PDFs and generating embeddings..."):
                all_text = ""

                for pdf in uploaded_files:
                    text = extract_text_from_pdf(pdf)

                    all_text += text + "\n"

                chunks = chunk_text(all_text, chunk_size=3000, overlap=300)

                embeddings = embedding_model.encode(
                    chunks, batch_size=128, show_progress_bar=True
                )

                st.session_state.chunks = chunks
                st.session_state.embeddings = embeddings

            st.success(f"Processed {len(uploaded_files)} PDF(s)")

            st.info(
                f"""
📄 Chunks Created: {len(chunks)}

📦 Chunk Size: 3000

🔍 Retrieval Chunks: 3
"""
            )

# -----------------------------
# Main UI
# -----------------------------

st.title("🎓 StudentAI")

st.caption("PDF RAG Chatbot using Streamlit + Ollama")

# -----------------------------
# Display Chat History
# -----------------------------

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# User Input
# -----------------------------

question = st.chat_input("Ask a question from your uploaded PDFs...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.markdown(question)

    if not st.session_state.chunks:
        answer = "Please upload and process PDF files first."

    else:
        retrieved_chunks = retrieve(question, top_k=3)

        context = "\n\n".join(retrieved_chunks)

        prompt = f"""
You are StudentAI.

Answer ONLY using the provided context.

If the answer is not present in the context,
say:

"I couldn't find that information in the uploaded notes."

Context:
{context}

Question:
{question}

Answer:
"""

        with st.spinner("🤔 StudentAI is thinking..."):
            answer = llm.invoke(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()

        words = answer.split()

        typed_text = ""

        for word in words:
            typed_text += word + " "

            placeholder.markdown(typed_text)

            time.sleep(0.03)

        if st.session_state.chunks:
            with st.expander("📄 Retrieved Context"):
                st.write(context)

    st.session_state.messages.append({"role": "assistant", "content": answer})
