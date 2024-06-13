# Use an official Python runtime as a parent image
FROM python:3.8-slim AS builder

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
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

ENV ENABLE_TESTING=false

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Environment variable to control testing
ENV ENABLE_TESTING=false

# Run entrypoint.py when the container launches
CMD ["python", "/app/entrypoint.py"]
