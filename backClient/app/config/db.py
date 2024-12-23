from dotenv import load_dotenv
import os


config = load_dotenv()

class DB:
    @staticmethod
    def get_db_url() -> str:
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')
        name = os.getenv('DB_NAME')
        password = os.getenv('DB_PASSWORD')
        user = os.getenv('DB_USER')

        return f"mysql+asyncmy://{user}:{password}@{host}:{port}/{name}"

