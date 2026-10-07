FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml README.md LICENSE server.py ./
RUN pip install --no-cache-dir .

RUN useradd --create-home appuser
USER appuser

# stdio by default. For HTTP / stdio por defecto. Para HTTP:
#   docker run -e MCP_TRANSPORT=http -p 8000:8000 astrologia-mcp
EXPOSE 8000
CMD ["astrologia-mcp"]
