# Contributing to StudentAI

Thank you for considering contributing to StudentAI! We welcome contributions of all kinds, including bug fixes, feature additions, documentation improvements, and more.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Code Style](#code-style)
- [Testing](#testing)
- [Pre-commit Hooks](#pre-commit-hooks)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)

## Code of Conduct

This project adheres to the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

1. Fork the repository.
2. Clone your fork:
   ```bash
   git clone https://code.swecha.org/sravani15/rag-chatbot.git
   cd rag-chatbot
   ```

## Development Setup

1. Ensure you have Python 3.13+ installed.
2. Install [uv](https://docs.astral.sh/uv/) (fast Python package manager).
3. Install project dependencies:
   ```bash
   uv sync --all-groups
   ```
4. Activate the virtual environment:
   - Linux/macOS: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`

## Code Style

- This project uses **Ruff** for linting and formatting.
- Run Ruff checks before committing:
  ```bash
  uv run ruff check .
  uv run ruff format . --check
  ```
- Additionally, **Pylint** is used for deeper static analysis:
  ```bash
  uv run pylint app.py manual_*.py
  ```

## Testing

- All tests are located in the `tests/` directory.
- Run tests with pytest:
  ```bash
  uv run pytest
  ```
- Ensure all tests pass before submitting a pull request.

## Pre-commit Hooks

This project uses pre-commit to enforce code quality. Install hooks:

```bash
uv run pre-commit install
```

The hooks will automatically run on every commit. You can also run them manually:

```bash
uv run pre-commit run --all-files
```

The following checks are enforced:

| Tool      | Purpose                        |
|-----------|--------------------------------|
| Ruff      | Linting and formatting         |
| Mypy      | Static type checking           |
| Pytest    | Test suite                     |
| Bandit    | Security vulnerability scan    |
| Pylint    | Code quality analysis          |
| Pyupgrade | Modern Python syntax upgrades  |
| Vulture   | Dead code detection            |
| Radon     | Code complexity analysis       |
| Semgrep   | Static application security    |

## Pull Request Process

1. Create a feature branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and ensure they pass all checks:
   ```bash
   uv run pre-commit run --all-files
   uv run pytest
   ```
3. Commit with a descriptive message:
   ```bash
   git commit -m "feat: add your feature description"
   ```
4. Push to your fork and open a merge request.
5. Ensure the merge request description clearly describes the problem and solution.

## Reporting Issues

- Use the issue tracker to report bugs or request features.
- Provide a clear description, steps to reproduce, and expected behavior.
- Include relevant logs, screenshots, or code snippets if applicable.
