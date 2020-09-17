from .base import Settings


class LocalSettings(Settings):
    # database settings
    db = {
        'drivername': 'mysql+pymysql',
        'username': 'root',
        'password': '!pwd4root',
        'host': 'localhost',
        'port': '3306',
        'database': 'fastival',
    }
