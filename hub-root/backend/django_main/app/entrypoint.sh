#!/bin/sh

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input -v 2 --clear

# python manage.py createcachetable

# if [ "$DJANGO_SUPERUSER_EMAIL" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ]
# then
#     python manage.py createsuperuser \
#         --noinput \
#         --email "$DJANGO_SUPERUSER_EMAIL"
# fi

# Execute the command passed as arguments
exec "$@"