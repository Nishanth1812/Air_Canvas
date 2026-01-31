#!/bin/bash
# Air Canvas Studio - Run Script
# Activates virtual environment and runs the application

cd "$(dirname "$0")"
source venv/bin/activate
python main.py
