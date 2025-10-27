#!/usr/bin/env bash
# Render build script

echo "Running migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating admin user if not exists..."
python manage.py createadmin
