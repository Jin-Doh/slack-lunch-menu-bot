FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY modules /app/modules
COPY utils /app/utils
COPY main.py /app/main.py

COPY pyproject.toml .
RUN poetry install

CMD ["poetry", "run", "python", "main.py"]
