# frontend/Dockerfile

FROM python:3.8-slim-buster

# Expose the Streamlit port
EXPOSE 8501

WORKDIR /app

# Copy all frontend files into the container
COPY . /app

# Upgrade pip and install frontend dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Start the Streamlit app on port 8501, binding to all network interfaces
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
