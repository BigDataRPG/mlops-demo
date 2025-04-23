FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Install the project in development mode
RUN pip install -e .

# Default command
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
