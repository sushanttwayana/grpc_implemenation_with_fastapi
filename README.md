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
