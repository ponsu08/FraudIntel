"""
Database Models
"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from database.database import Base


class FraudLog(Base):
    """
    Stores every prediction made by the system.
    """

    __tablename__ = "fraud_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    module = Column(
        String,
        nullable=False
    )

    input_data = Column(
        String,
        nullable=False
    )

    prediction = Column(
        String,
        nullable=False
    )

    confidence = Column(
        Float,
        nullable=False
    )

    risk = Column(
        String,
        nullable=False
    )

    explanation = Column(
        String,
        nullable=True
    )

    recommendation = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )