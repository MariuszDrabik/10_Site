#!/bin/sh

set -e

echo "Odpalamy apkę"

echo $ENV_TYPE

echo "Jedziemy"

echo pwd

# exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload
exec python3 new_www/main.py
