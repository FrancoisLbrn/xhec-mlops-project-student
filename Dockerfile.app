# Use Python 3.10 slim version
FROM python:3.10-slim

# Install the app dependencies
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy all of src into the /src folder
COPY ./src /src

# Copy the run_services.sh script into the /bin folder
COPY ./bin/run_services.sh /bin/run_services.sh

# Expose the correct ports (8001 for the API, 4200 for Prefect)
EXPOSE 8001 4200

# Make the run_services.sh script executable
RUN chmod +x /bin/run_services.sh

# Command to run the script
CMD ["/bin/run_services.sh"]
