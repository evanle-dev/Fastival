import os

from fastapi import FastAPI

from configurations.base import Settings

current_env: str = os.getenv('ENV', 'local')

if current_env == 'local':
    from configurations.local import LocalSettings

    settings: Settings = LocalSettings()
elif current_env == 'production':
    from configurations.production import ProductionSettings

    settings: Settings = ProductionSettings()

app = FastAPI(**settings.dict())

from .routes import *
