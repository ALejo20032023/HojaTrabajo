# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose Flask default port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
