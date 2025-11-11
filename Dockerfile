FROM python:3.14-alpine AS builder

WORKDIR /builder
# in case there is a needed build for wheels, these packages will come in handy (?)
RUN apk add build-base gfortran pkgconf openblas openblas-dev linux-headers
COPY requirements.txt .
RUN python -m venv /opt/venv
RUN --mount=type=cache,target=/root/.cache/pip \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install gunicorn -r ./requirements.txt

FROM python:3.14-alpine

LABEL org.opencontainers.image.title="Weather App" \
      org.opencontainers.image.description="A Python-based weather prediction service" \
      org.opencontainers.image.source="https://github.com/CMC-NCKH-2026/Weather_forcasting" \
      org.opencontainers.image.version="1.0.0"

WORKDIR /weather
ENV PORT="3636"
ENV GUNICORN_WORKERS=""
RUN adduser -D -h /weather weather && apk add --no-cache libgomp libstdc++ && rm -rf /var/cache/apk/*
COPY --from=builder --chown=weather:weather /opt/venv /opt/venv
COPY --chown=weather:weather . .
ENV PATH="/opt/venv/bin:$PATH"
RUN chmod +x /weather/src/scripts/docker-entrypoint.sh
USER weather
EXPOSE $PORT

ENTRYPOINT ["/weather/src/scripts/docker-entrypoint.sh"]