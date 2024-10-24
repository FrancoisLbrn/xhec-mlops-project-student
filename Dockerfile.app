# Dockerfile

# Use Python 3.10 slim version
FROM python:3.10-slim

# - install the app dependencies
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the application into the /web_service folder
COPY ./src/web_service /web_service

# Expose the correct ports (8001 for the API, 4201 if you want perfect Prefect)
EXPOSE 8001

# Set the working directory to /web_service
WORKDIR /web_service

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
