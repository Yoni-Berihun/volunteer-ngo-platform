from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
import uuid
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password_hash: Mapped[str]
    role: Mapped[str]  # VOLUNTEER | ORGANIZATION | ADMIN
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # One-to-one relationships
    volunteer_profile = relationship("VolunteerProfile", back_populates="user", uselist=False)
    organization_profile = relationship("OrganizationProfile", back_populates="user", uselist=False)