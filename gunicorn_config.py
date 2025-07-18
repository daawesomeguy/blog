# gunicorn_config.py
bind = "127.0.0.1:8000"
workers = 2
timeout = 30
keepalive = 2
max_requests = 1000
max_requests_jitter = 50
user = "pi"
group = "pi"
