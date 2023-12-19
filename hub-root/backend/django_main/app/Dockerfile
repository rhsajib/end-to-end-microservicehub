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
    pip install -r requirements.txt && \
    echo "Python dependencies installed successfully"

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/app/

RUN chmod +x /usr/src/app/entrypoint.sh 
  
ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]

# COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
# COPY ./wait-for-kafka.sh /usr/src/app/wait-for-kafka.sh

# COPY . /usr/src/app/

# RUN echo "Setting execute permissions" && \
#     chmod +x /usr/src/app/entrypoint.sh /usr/src/app/wait-for-kafka.sh && \
#     echo "Docker image built successfully"

# ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh", "/usr/src/app/wait-for-kafka.sh"]