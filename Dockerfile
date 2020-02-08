FROM dinutac/jinja2docker:2.1.3

COPY entrypoint.py /entrypoint.py

ENTRYPOINT ["/entrypoint.py"]
