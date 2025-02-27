# Base Python Image (Slim version for low memory usage)
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port 5000
EXPOSE 5000

# Reduce Gunicorn Workers to Save RAM
CMD ["gunicorn", "-w", "2", "--threads", "2", "-b", "0.0.0.0:5000", "app:app"]
