from sqlalchemy import Column, String, UnicodeText
from sqlalchemy.orm import declarative_base

BASE = declarative_base()


class Globals(BASE):
    __tablename__ = "globals"

    variable = Column(String, primary_key=True, nullable=False)
    value = Column(UnicodeText, nullable=False)

    def __init__(self, variable, value):
        self.variable = str(variable)
        self.value = value
