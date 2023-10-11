FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir -r requirements.txt

