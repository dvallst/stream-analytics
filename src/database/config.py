import os

from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', 'conf', '.env'))


class Config:
    HOST = os.getenv('DB_HOST')
    PORT = os.getenv('DB_PORT')
    USER = os.getenv('DB_USER')
    SECRET = os.getenv('DB_SECRET')
    DB = os.getenv('DB_NAME')
    SCHEMA = os.getenv('DB_SCHEMA')
    TABLE = os.getenv('DB_TABLE')

    @staticmethod
    def create_engine():
        return create_engine(f"postgresql://{Config.USER}:{Config.SECRET}@{Config.HOST}:{Config.PORT}/{Config.DB}")
