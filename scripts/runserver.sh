#!/bin/sh

if [ "$ENV" = "" ] || [ "$ENV" = "local" ]; then
  echo "You are running on local environment"
  uvicorn api:app --reload
else
  echo "You are running on $ENV environment"
  uvicorn api:app --host 0.0.0.0 --port 80
fi
