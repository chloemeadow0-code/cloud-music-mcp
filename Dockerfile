FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./
COPY src/ ./src/

RUN uv sync --frozen --no-dev

EXPOSE 8080

CMD ["uv", "run", "cloud-music-mcp", "--transport", "sse"]
