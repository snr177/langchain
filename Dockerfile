# Use the official Python image as a base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables (override in production as needed)
ENV PYTHONUNBUFFERED=1

# Default command: run the CLI chatbot (can be changed)
CMD ["python", "py files for basics/firebase-2.py"]
