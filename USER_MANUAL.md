# StudentAI User Manual

## Overview

StudentAI is a local Retrieval-Augmented Generation (RAG) chatbot designed for students. It allows you to upload PDF study materials and ask questions based on the uploaded content. All processing happens locally on your machine — no internet connection or API keys required.

## Table of Contents

- [Getting Started](#getting-started)
- [Uploading PDFs](#uploading-pdfs)
- [Asking Questions](#asking-questions)
- [Understanding Responses](#understanding-responses)
- [Managing Conversations](#managing-conversations)
- [Tips for Best Results](#tips-for-best-results)
- [Troubleshooting](#troubleshooting)
- [Technical Overview](#technical-overview)

## Getting Started

### Prerequisites

- Python 3.13 or higher
- A GGUF model file placed in the `models/` directory (default: `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf`)

### Installation

1. Install [uv](https://docs.astral.sh/uv/) (recommended) or use pip.
2. Clone or download the repository.
3. Install dependencies:
   ```bash
   uv sync --all-groups
   ```
4. Place a GGUF model file in the `models/` directory.
5. Launch the application:
   ```bash
   uv run streamlit run app.py
   ```

### System Requirements

- **RAM**: 4 GB minimum (8 GB recommended)
- **Storage**: 1 GB free space for the model and dependencies
- **OS**: Windows, macOS, or Linux

## Uploading PDFs

1. Open StudentAI in your browser (default: `http://localhost:8501`).
2. Locate the **Upload PDF** section in the left sidebar.
3. Click **Browse files** and select one or more PDF files.
4. Click the **Process PDFs** button.
5. Wait for the processing to complete. A success message will appear.

**Supported file types:** PDF only.

**Note:** The application does not support scanned PDFs or image-based PDFs. Only text-based PDFs will be processed successfully.

## Asking Questions

1. Type your question in the chat input box at the bottom of the screen.
2. Press Enter to submit.
3. Wait for the model to generate a response.
4. The response will appear in the chat area with a typewriter effect.

**Example questions:**

- "What is sales forecasting?"
- "Explain the sales planning process."
- "What are the steps in budgeting?"

## Understanding Responses

- Each response is generated based on the content of your uploaded PDFs.
- The model is instructed to answer only from the provided context.
- If the answer is not found in the documents, the model will respond: *"I could not find the answer in the document."*
- After each response, you can expand the **Retrieved Context** section to see which parts of the PDF were used.

## Managing Conversations

- **Clear Chat:** Click the **Clear Chat** button in the sidebar to reset the conversation.
- The chat history is preserved during the session but will be lost when you close the browser tab.

## Tips for Best Results

- **Upload relevant PDFs:** The model can only answer based on uploaded content.
- **Be specific:** Ask clear, specific questions for better results.
- **Use keywords:** Include relevant keywords from the document in your questions.
- **Limit PDF size:** Large PDFs may take longer to process. For best results, use focused study materials rather than entire textbooks.

## Troubleshooting

| Problem                      | Solution                                             |
|------------------------------|------------------------------------------------------|
| Model not found              | Ensure a GGUF model file exists in the `models/` directory. |
| PDF processing fails         | Ensure PDFs are text-based (not scanned images).     |
| Slow responses               | Reduce the number of uploaded PDFs or use a smaller model. |
| No answer in document        | Rephrase your question or check if the PDF contains the relevant information. |
| Streamlit won't start        | Verify all dependencies are installed (`uv sync`).   |

## Technical Overview

StudentAI follows a **local-first Mozilla-style workflow**:

```
PDF Upload → Text Extraction → Section Building → Keyword Retrieval → LLM Prompting → Answer
```

| Component       | Technology                |
|-----------------|---------------------------|
| PDF Extraction  | PyMuPDF4LLM               |
| Retrieval       | Keyword-based scoring     |
| Language Model  | llama.cpp (TinyLlama)     |
| Frontend        | Streamlit                 |
| Package Manager | uv                        |
