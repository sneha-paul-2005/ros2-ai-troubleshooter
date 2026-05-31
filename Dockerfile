# ROSA — ROS2 AI Assistant
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements-docker.txt .
RUN pip install --no-cache-dir -r requirements-docker.txt
# Copy all project files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV HF_HUB_OFFLINE=0
ENV TRANSFORMERS_VERBOSITY=error
ENV HF_HUB_DISABLE_PROGRESS_BARS=1

# Run Streamlit dashboard
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]