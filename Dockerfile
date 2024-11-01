FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

ENV PORT=8080


CMD ["sh", "-c", "alembic migrate head"]

# CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port $PORT"]