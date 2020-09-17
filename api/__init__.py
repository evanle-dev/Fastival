#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib

from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

__version__ = '0.1.0'

app = FastAPI()

version = __version__.split('.')

importlib.import_module('api.routes.v{0}_{1}'.format(version[1], version[2]))

app = VersionedFastAPI(app)
