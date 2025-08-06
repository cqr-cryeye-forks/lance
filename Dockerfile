FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .

RUN pip install --requirement requirements.txt

COPY . .
ENTRYPOINT ["python3", "lance.py", "--target", "example.com"]
