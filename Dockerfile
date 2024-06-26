FROM python:3.12-slim@sha256:541d45d3d675fb8197f534525a671e2f8d66c882b89491f9dda271f4f94dcd06

WORKDIR /app

COPY requirements.txt .
RUN  pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]