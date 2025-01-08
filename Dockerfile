FROM python:3.11-slim

WORKDIR /app
ENTRYPOINT ["/app/entrypoint.py"]

COPY poetry.lock pyproject.toml README.md ./
RUN pip install poetry \
 && poetry config virtualenvs.create false \
 && poetry install --no-root

COPY *.py ./
COPY test/ ./test
