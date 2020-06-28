#!/usr/bin/env bash

echo "Starting local server at: http://localhost:5000"


#python main/app.py
export FLASK_APP=main/app.py
export FLASK_ENV=development
flask run