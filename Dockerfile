# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Set the environment variables for email settings
ENV PYTHONPATH="/app"

# Copy the requirements file first to take advantage of Docker cache
COPY requirements.txt requirements.txt

# Install the dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Start the application using Waitress (as a WSGI server)
CMD ["waitress-serve", "--port=5000", "email_api.email_api:app"]
