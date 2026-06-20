FROM python:3.13-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock ./
RUN uv sync --all-groups --frozen

COPY . .

EXPOSE 8501

ENV MODEL_PATH=models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf

CMD ["uv", "run", "streamlit", "run", "app.py", "--server.headless", "true"]
