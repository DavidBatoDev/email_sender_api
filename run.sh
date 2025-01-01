#!/bin/bash
source venv/bin/activate
export FLASK_APP=email_api/email_api.py
export FLASK_ENV=production
flask run --host=0.0.0.0 --port=5000
