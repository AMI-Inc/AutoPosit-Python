FROM tiangolo/uvicorn-gunicorn:python3.8

WORKDIR /app

COPY requirements.frozen .
RUN pip install -r requirements.frozen

COPY app /app/app