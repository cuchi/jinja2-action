FROM python:3

RUN pip install poetry
COPY poetry.lock pyproject.toml /
RUN poetry install

COPY entrypoint.py /entrypoint.py

ENTRYPOINT ["/entrypoint.py"]
