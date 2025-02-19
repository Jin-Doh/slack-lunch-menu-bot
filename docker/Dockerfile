FROM python:3.12-slim

WORKDIR /app

ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY modules /app/modules
COPY utils /app/utils
COPY main.py /app/main.py

COPY pyproject.toml .
RUN poetry install

CMD ["python", "main.py"]
