# FastAPI + gRPC Restaurant Order System
This project demonstrates a simple microservices architecture using FastAPI as the API gateway and three gRPC servers (Bar, Bakery, Kitchen) to simulate a restaurant's order processing. The FastAPI app receives orders (drink, meal, dessert), validates them, and queries the gRPC servers for availability using mock stock data. It's built for learning gRPC with FastAPI, based on a blog post adapted with Conda for environment management.
Features

### FastAPI endpoint for creating orders with Pydantic validation (enums for items).
Three gRPC servers with protobuf-defined interfaces and mock stock checks.
Business logic to handle gRPC calls and aggregate responses (e.g., "Delivery!" or "out of stock").
Local and Dockerized setups for easy running and testing.

## 📁 Project Structure

<img width="662" height="529" alt="image" src="https://github.com/user-attachments/assets/fc2141b0-db30-4c37-b202-33f4b204bfc1" />


## Prerequisites

- Python 3.10+
- Conda (for local env)
- Docker and Docker Compose (for containerized setup)
- Git (for cloning)

## Setup (Local)

1. Clone this repository:

   ```bash
   git clone https://github.com/sushanttwayana/grpc_implemenation_with_fastapi.git
   cd grpc_fastapi
   ```
2. Create and activate Conda environment:

   ```bash
   git clone https://github.com/sushanttwayana/grpc_implemenation_with_fastapi.git
   cd grpc_fastapi
   ```
2.  Setup Virtual Env:

   ```bash
   conda create -n .venv python=3.10
   conda activate myenv
   ```

3. Install dependencies (run in root or each subfolder as needed; app has requirements.txt):

   ```bash
   cd app
   pip install -r requirements.txt
   For servers (bar, bakery, kitchen), install gRPC deps if not covered:
   pip install grpcio grpcio-tools grpc-interceptor python-dotenv
   ```
4. Generate protobuf files (run in each server folder, e.g., cd bar):
   ```bash
   textpython -m grpc_tools.protoc -I./protos --python_out=./pb --grpc_python_out=./pb ./protos/bar.proto
   Fix import in pb/*_grpc.py: Change import *_pb2 to import pb.*_pb2.
   Copy generated pb/ files to app/pb/.
   ```

**Fix import in pb/*_grpc.py: Change import *_pb2 to import pb.*_pb2.** 

**Copy generated pb/ files to app/pb/.**


## Running Locally
Open 4 terminals in the project root:

1. Bakery: cd bakery && python main.py (listens on 50051)
2. Bar: cd bar && python main.py (listens on 50052)
3. Kitchen: cd kitchen && python main.py (listens on 50053)
4. FastAPI: cd app && python main.py (runs on http://0.0.0.0:8000)

Servers log "Starter..." on success.

## Testing Locally
 ```bash
In a new terminal:
textcurl -X "POST" "http://127.0.0.1:8000/api/restaurants" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"drink\": \"coffee\", \"meal\": \"pasta\", \"dessert\": \"cookie\" }"

Expected: {"order_id":"uuid","drink":"Delivery!","meal":"Delivery!","dessert":"Delivery!"}
Test out-of-stock: Change to "beer", "pizza", "donut" → "out of stock" messages.
Invalid input: Non-enum values → 422 error.
```

## Docker Setup and Running

1. Ensure ports 8000, 50051-50053 are free (stop local servers).
2. Create network: docker network create my-net
3. Build and run: docker-compose up --build -d
   
   - Builds images and starts containers in background.
   - Logs: docker-compose logs -f


## Testing with Docker
```bash
Same curl as local:
textcurl -X "POST" "http://127.0.0.1:8000/api/restaurants" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"drink\": \"coffee\", \"meal\": \"pasta\", \"dessert\": \"cookie\" }"
Stop: docker-compose dow
```

## Output of Docker 

<img width="1557" height="785" alt="image" src="https://github.com/user-attachments/assets/2cc2f314-9d48-4812-9a6a-1a346fedf767" />


<img width="1571" height="820" alt="image" src="https://github.com/user-attachments/assets/ad8d57ed-c819-42d7-817b-4d80c56fde8c" />

<img width="1574" height="367" alt="image" src="https://github.com/user-attachments/assets/08681b54-d68f-40c3-81be-40f5399aaee4" />




