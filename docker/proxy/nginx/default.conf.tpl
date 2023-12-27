server {
    listen 80;
    server_name ${DOMAIN} www.${DOMAIN};

    location /.well-known/acme-challenge/ {
        root /vol/www/;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name ${DOMAIN} www.${DOMAIN};

    # SSL configuration goes here (certificate and key paths, etc.)

    # Serve static files
    location /static/ {
        alias /vol/static/;  # Ensure this directory matches the Docker volume for static files
    }

    # Serve media files
    location /media/ {
        alias /vol/media/;  # Ensure this directory matches the Docker volume for media files
    }

    location / {
        uwsgi_pass ${APP_HOST}:${APP_PORT};
        include uwsgi_params;
        client_max_body_size 10M;
    }
}
