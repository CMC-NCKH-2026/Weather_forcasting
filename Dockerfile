FROM python:3.14-alpine AS builder

WORKDIR /builder
# in case there is a needed build for wheels, these packages will come in handy (?)
RUN apk add build-base gfortran pkgconf openblas openblas-dev linux-headers
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && \
    pip install -r ./requirements.txt gunicorn

FROM python:3.14-alpine

LABEL org.opencontainers.image.title="Weather App" \
      org.opencontainers.image.description="A Python-based weather prediction service" \
      org.opencontainers.image.source="https://github.com/CMC-NCKH-2026/Weather_forcasting" \
      org.opencontainers.image.version="1.0.0"

WORKDIR /weather
ENV PORT "3636"
ENV GUNICORN_WORKERS ""
RUN adduser -D -h /weather weather
COPY --from=builder --chown=weather:weather /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages
COPY --chown=weather:weather . .
RUN chmod +x /weather/src/scripts/docker-entrypoint.sh
USER weather
EXPOSE $PORT

ENTRYPOINT ["/weather/src/scripts/docker-entrypoint.sh"]