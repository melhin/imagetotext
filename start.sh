#!/bin/bash

set -e

echo "Starting image renderer server..."

uvicorn main:app --host 0.0.0.0 --port $PORT --workers=4