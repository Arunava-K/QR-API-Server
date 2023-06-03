#!/bin/bash

# Clone the project
git clone https://github.com/Arunava-K/QR-API-Server.git

# Change to the project directory
cd QR-API-Server

# Build the Docker container
docker build -t qr-api .

# Run the Docker container
docker run -d -p 5000:5000 --name qr-api-container qr-api
