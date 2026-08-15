"""
Database Configuration

Creates the SQLite database and SQLAlchemy session.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///database/fraud_logs.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    """
    Dependency for FastAPI routes.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()