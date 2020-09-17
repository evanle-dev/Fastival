from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    title: str = 'Fastival'
    description: str = "This is a very fancy project, with auto docs for the API and everything"
    version: str = '1.0.0'
    split_version: List[int] = version.split('.')
    major_version: int = split_version[0]
    minor_version: int = split_version[1]
    build_version: int = split_version[2]
    openapi_url = '/api/v{}_{}/openapi.json'.format(major_version, minor_version)
    docs_url: str = '/api/v{}_{}/docs'.format(major_version, minor_version)
    redoc_url: str = '/api/v{}_{}/redoc'.format(major_version, minor_version)
