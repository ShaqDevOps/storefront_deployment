# FROM python:3.10-alpine3.16

# ENV PYTHONBUFFERED 1

# COPY requirements.txt /requirements.txt
# RUN apk add --upgrade --no-cache build-base linux-headers && \
#     pip install --upgrade pip && \
#     pip install -r /requirements.txt

# # Assuming your manage.py is in the storefront directory and that's the root of your project
# COPY . /app
# WORKDIR /app/storefront_deployment

# RUN adduser --disabled-password --no-create-home django

# USER django

# # Update the module to match your project's WSGI application
# CMD ["uwsgi", "--socket", ":8000", "--workers", "4", "--master", "--enable-threads", "--module", "storefront.wsgi"]


FROM python:3.10-alpine3.16

ENV PYTHONBUFFERED 1

RUN apk add --upgrade --no-cache build-base linux-headers libffi-dev openssl-dev mariadb-connector-c-dev

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install -r /requirements.txt

# Assuming your manage.py is in the storefront directory and that's the root of your project
COPY . /app
WORKDIR /app/storefront_deployment

RUN adduser --disabled-password --no-create-home django

USER django

# Update the module to match your project's WSGI application
CMD ["uwsgi", "--socket", ":8000", "--workers", "4", "--master", "--enable-threads", "--module", "storefront.wsgi"]
