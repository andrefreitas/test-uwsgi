# Test uwsgi vs non-uwsgi process behaviour
Test checking if process is running under uwsgi

## Setup
Configure `server.env` with the launch darkly key and then launch services:

    docker-compose up

## Usage
    curl http://0.0.0.0:9090 # uwsgi
    curl http://0.0.0.0:9091 # non-uwsgi