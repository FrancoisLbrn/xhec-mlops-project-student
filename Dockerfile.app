# Dockerfile

# Use Python 3.9.16 slim version
FROM python:3.9.16-slim

# - Install the app dependencies
RUN pip install --upgrade pip

# Copy the input file for pip-compile
COPY requirements.in ./requirements.in

# Install pip-tools and compile the requirements
RUN pip install pip-tools && pip-compile requirements.in

# Install the dependencies from the compiled requirements file
RUN pip install --no-cache-dir -r requirements_app.txt

# Copy the application into the /web_service folder
COPY ./src/web_service /web_service

# Copy the run_services.sh file from the bin directory
COPY ./bin/run_services.sh /run_services.sh

# Expose the correct ports (8001 for the API, 4201 for Prefect)
EXPOSE 8001 4201

# Give execution permissions to the run_services.sh script
RUN chmod +x /run_services.sh

# Set the working directory to /web_service
WORKDIR /web_service

# Run the services via the run_services.sh script
CMD ["/bin/bash", "/run_services.sh"]
