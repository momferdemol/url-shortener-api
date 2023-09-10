import string
from secrets import choice

from sqlalchemy.orm import Session

from . import crud
from .db import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_random_key(length: int = 5) -> str:
    chars = string.ascii_lowercase + string.digits
    return "".join(choice(chars) for _ in range(length))


def create_unique_random_key(db: Session) -> str:
    key = create_random_key()
    while crud.get_db_url_by_key(db, key):
        key = create_random_key()
    return key
