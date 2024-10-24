# Make sure to check bin/run_services.sh, which can be used here

# Do not forget to expose the right ports! (Check the PR_4.md)
FROM python:3.9.16-slim

# - install the app dependencies
RUN pip install --upgrade pip
COPY requirements.in ./
RUN pip install pip-tools && pip-compile requirements_app.in
RUN pip install --no-cache-dir -r requirements_app.txt

# Copy the application file into a dossier appelé /web_service
COPY ./web_service /web_service

# Expose les ports (8001 et 4201)
EXPOSE 8000 4201

# Setting the working directory to execute command
WORKDIR /web_service

# Lancer l'application avec uvicorn sur le port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
