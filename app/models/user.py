from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class User(Base):
    __tabename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    primary_email = Column(String, unique=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    organization_id = Column(ForeignKey("organization.id", ondelete="CASCADE"))
    last_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(String)
    updated_by = Column(String)

    organization = relationship("Organization", back_populates="users")
