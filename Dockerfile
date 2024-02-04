FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install the required Python packages
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the Flask app to the container
COPY main.py .
# Copy the .env file into the container at /app
COPY .env /app/
COPY . /app


# Set the command to run your application
CMD ["python", "main.py"]

