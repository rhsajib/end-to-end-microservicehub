#!/bin/bash

set -e

host="$1"
shift
cmd="$@"

until kafka-topics --list --bootstrap-server "$host" > /dev/null 2>&1; do
  >&2 echo "Kafka is unavailable - sleeping"
  sleep 1
done

>&2 echo "Kafka is up - executing command"
exec $cmd
