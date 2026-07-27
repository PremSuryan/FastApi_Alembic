from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:12345@localhost/fastapi"

engine = create_engine(DATABASE_URL)
session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit = False
)

Base = declarative_base()