import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()


class connectDB:

    @staticmethod
    def get_connect():
        try:
            cxn = psycopg2.connect(
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                database=os.getenv("POSTGRES_DB"),
                host=os.getenv("DB_HOST", "db"),
                port=int(os.getenv("DB_PORT", 5432))
            )
            return cxn
        except Exception as ex:
            print(f"Error al conectar: {ex}")
            return None
