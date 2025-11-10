FROM python:3.14-alpine AS builder
WORKDIR /builder
COPY requirements.txt .
RUN apk add build-base gfortran pkgconf openblas openblas-dev linux-headers
RUN pip3.14 install -r ./requirements.txt

FROM python:3.14-alpine
WORKDIR /weather
COPY . .
COPY --from=builder /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages
RUN adduser -D weather
USER weather
CMD ["python3.14", "./app.py"]