from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


class Base(DeclarativeBase):
    pass


engine = create_engine(
    url='postgresql+psycopg://postgres:12230@localhost:5432/Lab4',
    echo=True
)

session_factory = sessionmaker(engine)
