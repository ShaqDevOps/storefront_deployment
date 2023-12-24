
# FROM python:3.10-alpine3.16

# # Set environment variables
# ENV PYTHONUNBUFFERED 1
# ENV PYTHONPATH /app
# ENV DJANGO_SETTINGS_MODULE storefront.storefront.dev

# # Install dependencies
# RUN apk add --upgrade --no-cache build-base linux-headers libffi-dev openssl-dev mariadb-connector-c-dev pcre-dev

# # Install Python dependencies
# COPY requirements.txt /requirements.txt
# RUN pip install --no-cache-dir -r /requirements.txt

# # Copy the entire Django project into /app in the container
# # Ensure this includes manage.py and the storefront directory
# COPY ./storefront /app
# # COPY ./manage.py /app

# # Set the working directory to /app
# WORKDIR /app

# # Create a non-root user to run the Django app
# RUN adduser --disabled-password --no-create-home django
# USER django

# CMD ["uwsgi", "--socket", ":9000", "--workers", "4", "--master", "--enable-threads", "--module", "storefront.wsgi"]


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

# Create a non-root user
RUN adduser --disabled-password --no-create-home django

# Copy the entrypoint script and give execute permissions
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh



# Collect static files
# RUN python manage.py collectstatic --noinput

# Use the non-root user to run the app
USER django

# Set the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
