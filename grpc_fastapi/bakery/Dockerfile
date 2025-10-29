FROM python:3.10-slim

WORKDIR /home/bakery  

COPY . .

RUN pip install --no-cache-dir grpcio grpcio-tools grpc-interceptor python-dotenv

CMD ["python", "main.py"]