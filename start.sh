#!/bin/bash

set -e

echo "Downloading models..."
python download_language_models.py --source=de --target=en

echo "Starting image renderer server..."
uvicorn main:app --host 0.0.0.0 --port $PORT --workers=2
