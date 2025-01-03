{{- define "kauza.nginx.conf" -}}
worker_processes  auto;
worker_rlimit_nofile 10000;
error_log /dev/stdout info;
pid "/etc/nginx/nginx.pid";

events {
    worker_connections 4096;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log /dev/stdout;

    client_body_temp_path  "/etc/nginx/client_body" 1 2;
    proxy_temp_path        "/etc/nginx/proxy" 1 2;
    fastcgi_temp_path      "/etc/nginx/fastcgi" 1 2;
    scgi_temp_path         "/etc/nginx/scgi" 1 2;
    uwsgi_temp_path        "/etc/nginx/uwsgi" 1 2;

    sendfile        on;

    keepalive_timeout  65;

    gzip on;
    gzip_vary on;
    gzip_min_length 1400;
    gzip_proxied expired no-cache no-store private auth;
    gzip_types text/plain text/css text/xml text/javascript application/javascript application/json application/x-javascript application/xml;

    include /etc/nginx/conf.d/*.nginx.conf;

    # allow the server to close connection on non responding client, this will free up memory
    reset_timedout_connection on;

    # request timed out -- default 60
    client_body_timeout 10;

    # if client stop responding, free up memory -- default 60
    send_timeout 2;

    # server will close connection after this time -- default 75
    proxy_read_timeout 3600;

    # number of requests client can make over keep-alive -- for testing environment
    keepalive_requests 100000;

    # whether the connection with a proxied server should be closed
    # when a client closes the connection without waiting for a response
    # default is off
    proxy_ignore_client_abort on;
    server_tokens off;

    # Disallow indexing
    add_header X-Robots-Tag none;
}
{{- end -}}
