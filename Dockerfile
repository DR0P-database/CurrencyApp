FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /docker_app

COPY requirements.txt .
RUN  pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "currency_app.app:app"]
# CMD python main.py