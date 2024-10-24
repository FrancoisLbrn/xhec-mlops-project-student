#!/bin/bash
# Set Prefect API URL to be accessible at 0.0.0.0:4200
prefect config set PREFECT_API_URL=http://0.0.0.0:4200/api

# Start Prefect server in the background
prefect server start --host 0.0.0.0 --port 4200 &

# Navigate to the correct directory
cd /web_service  # Make sure this path is correct

# Start FastAPI with Uvicorn on port 8001
uvicorn main:app --host 0.0.0.0 --port 8001
