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

## How It Works
MCP follows a client-server architecture:

- MCP Server - Exposes tools, resources, and capabilities
- MCP Client - Connects AI models to servers
- AI Model - Uses tools via MCP to complete tasks

<img width="520" height="150" alt="image" src="https://github.com/user-attachments/assets/0be91307-4d1e-48cf-bd94-dc6c070bb72e" />

## Use Cases

- Personal Finance Management - Track expenses with AI
- Conversational AI - Build chatbots with tool access
- Data Analysis - Query databases through natural language
- Automation - Create AI agents that interact with APIs
- Content Generation - Generate animations or visualizations

### Technologies Used

- Python - Core language
- FastMCP - Python MCP framework
- LangGraph - Agent orchestration
- SQLite - Database for expense tracker
- Manim - Mathematical animations

## Project Structure Explained
Each folder contains a complete MCP implementation:

- server.py or main.py - MCP server implementation
- client.py - MCP client (if separate)
- requirements.txt - Dependencies
- README.md - Project-specific documentation


