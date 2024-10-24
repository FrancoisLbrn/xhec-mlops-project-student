prefect config set PREFECT_API_URL=http://0.0.0.0:4200/api

sqlite3 --version

# Start Prefect server in the background
prefect server start --host 0.0.0.0 &

# Go in the good directory
cd ../src/web_service

# Start FastAPI with Uvicorn
uvicorn main:app --reload --port 8001
