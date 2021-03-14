from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class User(Base):
    """ The User base class contains common User data."""
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    hashedPassword = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow, nullable=False)