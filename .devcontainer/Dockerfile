FROM mcr.microsoft.com/devcontainers/python:3.12

# Set working directory
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose Flask default port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Default command
# CMD ["python", "run.py"]
# for production use gunicorn
# CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
