# Dockerfile

FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Introduce an error
RUN invalid_command

# Expose the port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
