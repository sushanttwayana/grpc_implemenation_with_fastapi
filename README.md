# FastAPI + gRPC Restaurant Order System
This project demonstrates a simple microservices architecture using FastAPI as the API gateway and three gRPC servers (Bar, Bakery, Kitchen) to simulate a restaurant's order processing. The FastAPI app receives orders (drink, meal, dessert), validates them, and queries the gRPC servers for availability using mock stock data. It's built for learning gRPC with FastAPI, based on a blog post adapted with Conda for environment management.
Features

### FastAPI endpoint for creating orders with Pydantic validation (enums for items).
Three gRPC servers with protobuf-defined interfaces and mock stock checks.
Business logic to handle gRPC calls and aggregate responses (e.g., "Delivery!" or "out of stock").
Local and Dockerized setups for easy running and testing.

## Project Structure

grpc_fastapi/
├── app/                  # FastAPI application
│   ├── api/
│   │   ├── dependencies/
│   │   │   └── grpc/     # gRPC clients (bar.py, bakery.py, kitchen.py)
│   │   ├── routes/       # API routes (restaurants.py)
│   │   └── router.py
│   ├── business_logic/   # Order processing logic (restaurants.py)
│   ├── core/             # Config (config.py)
│   ├── pb/               # Generated protobuf files
│   ├── schemas/          # Pydantic models (orders.py)
│   ├── .env              # Environment variables
│   ├── Dockerfile        # Docker build for FastAPI
│   ├── main.py           # FastAPI entry point
│   └── requirements.txt  # Pip dependencies
├── bar/                  # gRPC Bar server (similar for bakery/ and kitchen/)
│   ├── core/             # Config
│   ├── pb/               # Generated protobuf
│   ├── protos/           # Proto definitions (bar.proto)
│   ├── services/         # Service logic (bar.py)
│   ├── .env
│   ├── Dockerfile
│   └── main.py
├── bakery/               # gRPC Bakery server
├── kitchen/              # gRPC Kitchen server
├── docker-compose.yaml   # Docker Compose for all services
├── .gitignore            # Git ignores
└── README.md             # This file
