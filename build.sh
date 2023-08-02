#!/usr/bin/env bash
# exit on error
set -o errexit

python .\setup_env.py
pip install -r requirements.txt
python manage.py migrate
