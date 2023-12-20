# Use the base image with Python
FROM python:3.10-alpine3.16

# Set environment variables
ENV PYTHONBUFFERED 1

# Install system dependencies
RUN apk --no-cache add build-base linux-headers mariadb-dev

# Create a directory for your application
RUN mkdir /app

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . /app/

# Create a non-root user to run the application
RUN adduser --disabled-password --no-create-home django
USER django

# Update the module to match your project's WSGI application
CMD ["uwsgi", "--socket", ":8000", "--workers", "4", "--master", "--enable-threads", "--module", "storefront.wsgi"]
