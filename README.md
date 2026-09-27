# StudentAI 🎓

## Local-First Intelligent Document Question Answering System

StudentAI is a privacy-first Artificial Intelligence application that enables users to upload PDF documents and interact with them using natural language queries.

The system follows a Retrieval-Augmented Question Answering approach that retrieves relevant information from uploaded documents before generating responses through a locally running Large Language Model (LLM).

Unlike cloud-based AI solutions, StudentAI follows a local-first architecture where all document processing, retrieval, and AI inference occur on the user's machine. This ensures privacy, security, offline accessibility, and complete ownership of user data.

---

## Project Status

- ✅ Functional PDF Question Answering System
- ✅ Local Large Language Model Integration
- ✅ GitLab CI/CD Pipeline
- ✅ Automated Testing
- ✅ Security Scanning
- ✅ Static Code Analysis
- ✅ Open-Source Documentation
- ✅ AGPL-3.0 Licensed
- ✅ 100% Compliance Score

---

## Features

- PDF Document Upload
- PDF Text Extraction using PyMuPDF4LLM
- Section-Based Document Processing
- Keyword-Based Document Retrieval
- Context-Aware Answer Generation
- Local LLM Inference using llama.cpp
- Interactive Chat Interface
- Retrieved Context Viewer
- Typewriter Response Rendering
- Privacy-First Design
- Offline Operation
- Automated Testing and Validation
- GitLab CI/CD Integration
- Security Compliance Checks

---

## System Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                     User (Browser)                          │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Streamlit Frontend                         │
│                                                             │
│   PDF Upload → Chat Interface → Context Viewer             │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Application Layer                          │
│                                                             │
│  Document Processing                                        │
│  Section Builder                                            │
│  Retrieval Module                                           │
│  Prompt Construction                                        │
│  Response Generation                                        │
└───────────────┬───────────────────────┬─────────────────────┘
                │                       │
                ▼                       ▼
┌──────────────────────┐   ┌───────────────────────────────┐
│      PyMuPDF4LLM     │   │         llama.cpp             │
│   PDF → Markdown     │   │    Local LLM Inference        │
└──────────────────────┘   └───────────────────────────────┘
```

---

## Workflow

```text
PDF Upload
      │
      ▼
PyMuPDF4LLM Extraction
      │
      ▼
Markdown Conversion
      │
      ▼
Section Builder
      │
      ▼
User Question
      │
      ▼
Keyword-Based Retrieval
      │
      ▼
Top Relevant Sections
      │
      ▼
Prompt Construction
      │
      ▼
TinyLlama (llama.cpp)
      │
      ▼
Generated Response
      │
      ▼
Streamlit Interface
```

---

## Retrieval Mechanism

StudentAI uses a lightweight keyword-based retrieval approach.

The uploaded PDF is converted into structured Markdown and divided into logical sections. When a user submits a question:

1. The query is tokenized into keywords.
2. Each document section is compared against the query.
3. Sections receive scores based on keyword overlap.
4. Top-matching sections are selected.
5. Retrieved context is supplied to the language model.
6. The model generates an answer using the retrieved content.

This retrieval-augmented workflow improves answer relevance while maintaining a lightweight and fully local implementation.

---

## Installation

### Prerequisites

- Python 3.13+
- uv Package Manager
- GGUF Model File

Example model:

```text
tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf
```

Place the model inside:

```text
models/
```

### Clone Repository

```bash
git clone https://code.swecha.org/sravani15/rag-chatbot.git
cd rag-chatbot
```

### Install Dependencies

```bash
uv sync --all-groups
```

### Run Application

```bash
uv run streamlit run app.py
```

### Open Browser

```text
http://localhost:8501
```

---

## Usage

### Step 1
Upload one or more PDF documents.

### Step 2
Process the uploaded documents.

### Step 3
Wait for text extraction and document processing.

### Step 4
Ask questions related to the uploaded document.

### Step 5
Review the generated response and retrieved context.

---

## Technologies Used

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.13+ |
| User Interface | Streamlit |
| PDF Processing | PyMuPDF4LLM |
| Retrieval System | Custom Keyword-Based Retrieval |
| LLM Inference | llama.cpp |
| Language Model | TinyLlama GGUF |
| Package Manager | uv |
| Version Control | Git |
| Repository Hosting | GitLab |
| CI/CD | GitLab CI/CD |

---

## Compliance & Quality Assurance

StudentAI was developed following open-source software engineering practices and successfully achieved a **100% Compliance Score** using the Swecha Project Compliance Framework.

The project includes:

- Project Documentation Standards
- Security Policies
- License Compliance
- Contribution Guidelines
- Continuous Integration
- Automated Testing
- Static Analysis
- Security Scanning
- Code Quality Validation

---

## Quality Assurance Tools

| Tool | Purpose |
|--------|----------|
| Ruff | Linting & Formatting |
| Flake8 | Style Validation |
| Pylint | Code Quality Analysis |
| Mypy | Static Type Checking |
| Pytest | Automated Testing |
| Bandit | Security Scanning |
| Semgrep | Static Application Security Testing |
| Gitleaks | Secret Detection |
| Pyupgrade | Python Modernization |
| Vulture | Dead Code Detection |
| Radon | Complexity Analysis |

---

## Testing

Install pre-commit hooks:

```bash
uv run pre-commit install
```

Run all validation checks:

```bash
uv run pre-commit run --all-files
```

Run tests:

```bash
uv run pytest
```

Coverage includes:

- Section Generation
- Retrieval Logic
- Question Answering Workflow
- Application Validation

---

## Continuous Integration (CI/CD)

StudentAI uses GitLab CI/CD pipelines to automatically validate every change pushed to the repository.

### Pipeline Stages

```text
Lint
 ↓
Format
 ↓
Type Check
 ↓
Security Scan
 ↓
Testing
 ↓
Coverage
```

### Automated Validation

- Ruff
- Flake8
- Pylint
- Mypy
- Bandit
- Pytest
- Coverage Analysis

Every commit must successfully pass all validation stages before integration.

---

## Security

StudentAI incorporates multiple security validation layers:

- Bandit Security Analysis
- Semgrep Security Scanning
- Gitleaks Secret Detection
- Dependency Auditing
- Pre-Commit Validation

These tools help identify vulnerabilities, insecure coding patterns, and accidental secret exposure.

---

## Mozilla Local-First Principles

StudentAI follows Mozilla's Local-First philosophy.

### Benefits

- No external AI APIs
- No cloud dependency
- No user tracking
- Offline functionality
- Complete data ownership
- Enhanced privacy and security

All uploaded documents remain on the user's machine throughout processing and response generation.

---

## Internship Context

This project was developed during the Artificial Intelligence Internship conducted by VISWAM.AI and Swecha Foundation.

### Internship Focus Areas

- Artificial Intelligence Applications
- Intelligent Document Processing
- Retrieval-Augmented Generation (RAG)
- Local AI Systems
- Open Source Software Development
- GitLab CI/CD Workflows
- Software Quality Assurance
- Project Compliance Standards

The project provided practical experience in building AI-powered applications while following modern software engineering practices.

---

## Project Highlights

- Developed during the VISWAM.AI / Swecha Artificial Intelligence Internship
- Built as a Local-First Intelligent Document Question Answering System
- Processes PDF documents entirely offline
- Uses Retrieval-Augmented Generation (RAG)
- Integrates local LLM inference through llama.cpp
- Implements automated testing and security validation
- Uses GitLab CI/CD for continuous integration
- Achieved 100% Compliance Score
- Follows Mozilla Local-First principles

---

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).

---

## Security Policy

See `SECURITY.md` for vulnerability reporting guidelines and security practices.

---

## Author

**Sravani Jagarlamudi**

Artificial Intelligence Intern

VISWAM.AI – Centre of Excellence on AI for the Global South

Swecha Foundation & IIIT Hyderabad
