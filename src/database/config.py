import os

from dotenv import load_dotenv


class Config:
    load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', 'conf', '.env'))

    HOST = os.getenv('DB_HOST')
    PORT = os.getenv('DB_PORT')
    USER = os.getenv('DB_USER')
    SECRET = os.getenv('DB_SECRET')
    DB = os.getenv('DB_NAME')
