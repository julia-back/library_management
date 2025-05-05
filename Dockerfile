FROM python:3.12-slim

RUN mkdir -p /app \
    && mkdir -p /app/media \
    && mkdir -p /app/static

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry --no-cache-dir

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root

COPY . .

EXPOSE 8000
