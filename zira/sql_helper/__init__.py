import time

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import scoped_session, sessionmaker

from .core.base import BASE

DB_URL = "postgresql+psycopg2://postgres:{password}@postgres.railway.internal:5432/railway".format(
    password=os.getenv("PGPASSWORD")
)


def start():
    for i in range(10):
        try:
            engine = create_engine(DB_URL)
            conn = engine.connect()
            conn.close()
            break
        except OperationalError:
            print(f"[DB] Not ready yet — retry {i+1}/10")
            time.sleep(5)
    else:
        raise Exception("Database not ready after retries")

    BASE.metadata.create_all(engine)

    session_factory = sessionmaker(bind=engine, autoflush=False)
    return scoped_session(session_factory)


SESSION = start()
