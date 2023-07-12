#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install --no-root
python manage.py migrate
waitress-serve --listen=*:8000 wsgi:application
