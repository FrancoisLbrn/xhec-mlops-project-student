#!/bin/bash
# Set Prefect API URL to be accessible at 0.0.0.0:4201
prefect config set PREFECT_API_URL=http://0.0.0.0:4200/api

# Start Prefect server in the background
prefect server start --host 0.0.0.0 --port 4200 &

# Navigate to the correct directory
cd /src/web_service  # Make sure this path is correct

# Start FastAPI with Uvicorn on port 8000
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Wait for Prefect server to be live before running deployment.py
sleep 10

# Run deployment.py to train model regularly in Prefect
cd /src/modelling
python3 deployment.py
