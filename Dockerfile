FROM python:3.14-alpine AS builder

WORKDIR /builder
# in case there is a needed build for wheels, these packages will come in handy (?)
RUN apk add build-base gfortran pkgconf openblas openblas-dev linux-headers
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && \
    pip install scikit-learn numpy pandas flask gunicorn

FROM python:3.14-alpine

LABEL org.opencontainers.image.title="Weather App" \
      org.opencontainers.image.description="A Python-based weather prediction service" \
      org.opencontainers.image.source="https://github.com/CMC-NCKH-2026/Weather_forcasting" \
      org.opencontainers.image.version="1.0.0"

WORKDIR /weather
ENV PORT="3636"
ENV GUNICORN_WORKERS=""
RUN adduser -D -h /weather weather && apk add --no-cache libgomp libstdc++ && rm -rf /var/cache/apk/*
COPY --from=builder /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn
COPY --chown=weather:weather . .
USER weather
EXPOSE $PORT

ENTRYPOINT ["/weather/src/scripts/docker-entrypoint.sh"]