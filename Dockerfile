FROM python:3.11

WORKDIR /app
ENTRYPOINT ["/app/entrypoint.py"]

COPY poetry.lock pyproject.toml ./
RUN pip install --no-cache-dir poetry==1.8.5 \
 && poetry config virtualenvs.create false \
 && poetry install

COPY . ./
