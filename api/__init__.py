import os

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

# Get configuration based on the environment
current_env: str = os.getenv('ENV', 'local')
if current_env == 'local':
    from configurations.local import LocalSettings

    settings: LocalSettings = LocalSettings()
elif current_env == 'production':
    from configurations.production import ProductionSettings

    settings: ProductionSettings = ProductionSettings()

# Create new app
app = FastAPI(**settings.dict())

# Database connection
engine = create_engine(URL(**settings.db))
try:
    engine.connect()
    print('Connect to database successful!')
except:
    print('Connect to database failure! Please check database configurations again!')

from .routes import *
