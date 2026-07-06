FROM python:3.12-slim

WORKDIR /app

# Install git (needed for pyncm git dependency) and uv
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir uv

# Copy project files
COPY . .

# Install dependencies
RUN uv sync --no-dev

EXPOSE 8080

CMD ["uv", "run", "cloud-music-mcp", "--transport", "sse"]
