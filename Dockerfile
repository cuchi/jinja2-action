FROM python:3

WORKDIR /app
ENTRYPOINT ["/app/entrypoint.py"]

COPY poetry.lock pyproject.toml ./
RUN pip install poetry \
 && poetry config virtualenvs.create false \
 && poetry install

COPY . ./
