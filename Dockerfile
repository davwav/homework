# Use an official Python runtime as a parent image
FROM python:3.8-slim AS builder

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y gcc python3-dev

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Runtime image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the built dependencies from the previous stage
COPY --from=builder /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/

# Copy the application code
COPY . .

# Command to run the application
ENTRYPOINT ["python", "app.py"]
CMD [ "output", "pids"]

