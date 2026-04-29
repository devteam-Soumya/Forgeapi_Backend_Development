FROM python:3.13-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV APP_MODULE=generated.backend.main_public:app

CMD ["sh", "-c", "uvicorn $APP_MODULE --host 0.0.0.0 --port 8000"]
