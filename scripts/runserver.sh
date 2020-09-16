#!/bin/sh

if [ "$ENV" != "" ]; then
  echo "You are running on $ENV environment"
  uvicorn api:app --host 0.0.0.0 --port 80
else
  echo "You are running on local environment"
  uvicorn api:app --reload
fi
