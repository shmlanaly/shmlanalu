import os
import time

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import scoped_session, sessionmaker

DB_URL = os.getenv("DATABASE_URL")


def start():
    for i in range(5):
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

    session_factory = sessionmaker(bind=engine, autoflush=False)
    return scoped_session(session_factory)


SESSION = start()

from .globals import BASE, Globals

# Create tables
BASE.metadata.create_all(SESSION.get_bind())


# ===== Helper Functions =====


def gvarstatus(variable):
    obj = SESSION.query(Globals).filter(Globals.variable == str(variable)).first()
    return obj.value if obj else None


def addgvar(variable, value):
    old = SESSION.query(Globals).filter(Globals.variable == str(variable)).one_or_none()
    if old:
        SESSION.delete(old)

    new = Globals(variable, value)
    SESSION.add(new)
    SESSION.commit()


def delgvar(variable):
    obj = SESSION.query(Globals).filter(Globals.variable == str(variable)).one_or_none()
    if obj:
        SESSION.delete(obj)
        SESSION.commit()
