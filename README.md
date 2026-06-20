# StudentAI 🎓

**Local Retrieval-Augmented Generation (RAG) Chatbot for Students**

StudentAI is a privacy-first, local document Q&A application. Upload PDF study materials and ask questions — the system retrieves relevant content and generates answers using a local LLM. No internet connection, no API costs, no data leaves your machine.

---

## Features

- **PDF Upload & Extraction** — Upload one or more PDF files; text is automatically extracted using PyMuPDF4LLM.
- **Section-Based Retrieval** — Documents are split into logical sections; keyword scoring finds the most relevant content for your question.
- **Local LLM Inference** — Uses llama.cpp with a TinyLlama GGUF model. Everything runs on your machine.
- **Typewriter Response** — Answers are rendered word-by-word for a natural reading experience.
- **Retrieved Context Display** — Expand to see exactly which parts of the document were used to generate the answer.
- **Clear Chat** — Reset the conversation with one click.
- **Streamlit UI** — Clean, responsive web interface.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     User (Browser)                          │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Streamlit Frontend                          │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │ PDF Upload  │  │ Chat Panel   │  │ Context Viewer   │   │
│  └──────┬──────┘  └──────┬───────┘  └──────────────────┘   │
└─────────┼────────────────┼──────────────────────────────────┘
          │                │
          ▼                ▼
┌─────────────────────────────────────────────────────────────┐
│                    Application Logic                         │
│  ┌──────────────────┐  ┌────────────────────────────────┐   │
│  │ Section Builder  │  │ Keyword Retrieval              │   │
│  │ (re.split on ##) │  │ (word overlap scoring, top_k)  │   │
│  └────────┬─────────┘  └───────────────┬────────────────┘   │
└───────────┼────────────────────────────┼────────────────────┘
            │                            │
            ▼                            ▼
┌─────────────────────┐  ┌────────────────────────────────────┐
│  PyMuPDF4LLM        │  │  llama.cpp (TinyLlama GGUF)        │
│  (PDF → Markdown)   │  │  (Prompt + Context → Answer)       │
└─────────────────────┘  └────────────────────────────────────┘
```

**Data Flow:**

```
PDF Upload → PyMuPDF4LLM → Markdown Text
    → Section Builder (split by ## headings)
    → User Question
    → Keyword Retrieval (score sections by word overlap)
    → Top-k Sections → Context Truncation (1500 chars)
    → LLM Prompt (Context + Question)
    → Generated Answer → Streamlit UI (typewriter effect)
```

---

## Installation

### Prerequisites

- Python 3.13 or higher
- A GGUF model file in the `models/` directory (default: `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf`)

### Setup

1. **Install uv** (fast Python package manager):

   ```bash
   pip install uv
   ```

2. **Clone the repository:**

   ```bash
   git clone https://code.swecha.org/sravani15/rag-chatbot.git
   cd rag-chatbot
   ```

3. **Install dependencies:**

   ```bash
   uv sync --all-groups
   ```

4. **Place a GGUF model file** in `models/`. You can download TinyLlama:

   ```bash
   # Example using a TinyLlama GGUF model
   # Place the file at: models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf
   ```

5. **Run the application:**

   ```bash
   uv run streamlit run app.py
   ```

6. **Open your browser** to `http://localhost:8501`.

---

## Usage

1. Open StudentAI in your browser.
2. In the sidebar, click **Browse files** to upload one or more PDF files.
3. Click **Process PDFs** to extract and index the content.
4. Type your question in the chat input and press Enter.
5. View the answer and expand **Retrieved Context** to see source material.

---

## Pre-commit

This project uses [pre-commit](https://pre-commit.com/) to enforce code quality. Install the hooks:

```bash
uv run pre-commit install
```

Run all hooks manually:

```bash
uv run pre-commit run --all-files
```

The following checks are enforced:

| Tool      | Category              | Purpose                         |
|-----------|-----------------------|---------------------------------|
| Ruff      | Linting & Formatting  | Code style and quality          |
| Mypy      | Type Checking         | Static type analysis            |
| Pytest    | Testing               | Test suite execution            |
| Bandit    | Security              | Vulnerability scanning          |
| Pylint    | Code Quality          | Deep static analysis            |
| Pyupgrade | Modernization         | Python syntax upgrades          |
| Vulture   | Dead Code             | Unused code detection           |
| Radon     | Complexity            | Cyclomatic complexity analysis  |
| Semgrep   | SAST                  | Static application security     |

---

## Testing

Run the test suite with pytest:

```bash
uv run pytest
```

Tests are located in the `tests/` directory. Coverage includes:

- Section building from markdown text
- Retrieval logic (keyword-based scoring)

---

## Technologies

| Component               | Technology                      |
|-------------------------|---------------------------------|
| Programming Language    | Python 3.13+                    |
| Web Framework           | Streamlit                       |
| PDF Extraction          | PyMuPDF4LLM                     |
| LLM Inference           | llama.cpp (via llama-cpp-python)|
| Model                   | TinyLlama 1.1B (GGUF)           |
| Package Manager         | uv                              |
| Linting                 | Ruff, Pylint                    |
| Type Checking           | Mypy                            |
| Testing                 | Pytest                          |
| Security                | Bandit, Semgrep                 |
| Dead Code Detection     | Vulture                         |
| Code Complexity         | Radon                           |
| Pre-commit              | Pre-commit                      |

---

## Mozilla Local-First Workflow

StudentAI follows the **Mozilla local-first** philosophy:

- **No external APIs** — All LLM inference runs locally via llama.cpp.
- **No data transmission** — PDFs are processed entirely on your machine.
- **No account required** — No sign-up, no login, no tracking.
- **Offline-capable** — Once dependencies and model are downloaded, the application works fully offline.
- **Privacy by design** — Your study materials never leave your computer.

This approach aligns with Mozilla's principles of putting users in control of their data and computing experience.

---

## License

This project is licensed under the MIT License.

---

## Security

See [SECURITY.md](SECURITY.md) for our security policy and vulnerability reporting guidelines.
