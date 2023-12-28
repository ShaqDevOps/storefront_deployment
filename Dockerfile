FROM python:3.10-alpine3.16

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app
ENV DJANGO_SETTINGS_MODULE storefront.storefront.dev

# Install system dependencies
RUN apk add --upgrade --no-cache build-base linux-headers libffi-dev openssl-dev mariadb-connector-c-dev pcre-dev

# Install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy the entire Django project
COPY ./storefront /app

# Set the working directory
WORKDIR /app

# Create a non-root user and change ownership
RUN adduser --disabled-password --no-create-home django \
    && chown -R django:django /app

# Copy the entrypoint script and give execute permissions
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Use the non-root user to run the app
USER django

# Set the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
