# StudentAI Constitution

## Purpose

StudentAI is a local-first document question-answering system designed to help students interact with PDF study materials.

## Principles

1. Local-first processing whenever possible.
2. User documents remain on the user's machine.
3. Retrieval should be explainable and reproducible.
4. Code quality must be enforced through:

   * Ruff
   * Mypy
   * Pytest
   * Pre-commit
5. New features should be documented before implementation.

## Architecture

PDF Upload → Extraction → Section Parsing → Retrieval → Answer Generation

## Quality Requirements

* All code must pass linting.
* All code must pass formatting checks.
* All code must pass type checking.
* Unit tests are required for core functionality.
