# backend/Dockerfile

FROM python:3.8-slim-buster

# Expose the Flask API port
EXPOSE 5000

WORKDIR /app

# Copy all backend files into the container
COPY . /app

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run the Flask application
CMD ["python", "app.py"]
