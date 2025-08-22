# Base image
FROM python:3.12-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Ensure wait-for-db.sh is executable
RUN chmod +x /app/wait-for-db.sh

# Run server with wait-for-db
CMD ["sh", "-c", "/app/wait-for-db.sh db:5432 && python manage.py migrate && python manage.py populate_initial_data && python manage.py runserver 0.0.0.0:8000"]

