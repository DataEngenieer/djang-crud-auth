#!/bin/bash
pip install --upgrade pip
pip install -r requirements.txt
# exit on error
set -o errexit



# poetry install

# pip install --upgrade pip


python manage.py collectstatic --no-input
python manage.py migrate