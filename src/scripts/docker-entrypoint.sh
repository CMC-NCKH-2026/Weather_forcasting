#!/bin/sh

set -e
: "${PORT:=3636}"

# runs with exec for pid1 enabling better docker process management

if [ "$PURE_FLASK" = "true" ]; then
  exec python3 app.py -p $PORT
else
  if [ -z "$GUNICORN_WORKERS" ]; then
    WORKERS=$(( $(nproc) / 2 ))
    if [ "$WORKERS" -lt 1 ]; then
      WORKERS=1
    fi
  else
    WORKERS=$GUNICORN_WORKERS
  fi
  exec gunicorn -w "$WORKERS" -b 0.0.0.0:$PORT app:app
fi