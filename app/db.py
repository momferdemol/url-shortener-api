from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings

engine = create_engine(
    get_settings().db_url,
    # check_same_thread to allow multiple requests at the same time
    connect_args={"check_same_thread": False},
)

# create a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# connect the database engine to the models
Base = declarative_base()
