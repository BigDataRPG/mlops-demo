FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry && poetry install --no-interaction --no-ansi

COPY . .

CMD ["poetry", "run", "python", "src/app.py"]
