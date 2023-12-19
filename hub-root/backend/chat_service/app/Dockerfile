FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

# Install system dependencies for kafka
# https://stackoverflow.com/questions/43664505/using-confluent-kafka-python-client-in-alpine-container
RUN echo "Installing system dependencies" && \
    sed -i -e 's/v3\.4/edge/g' /etc/apk/repositories && \
    apk upgrade --update-cache --available && \
    apk add gcc libc-dev librdkafka-dev && \
    echo "System dependencies installed successfully"

COPY ./requirements.txt /usr/src/app/requirements.txt

# Upgrade pip and install Python dependencies
RUN echo "Upgrading pip and installing Python dependencies" && \
    pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

COPY . /usr/src/app/
