import uuid
from datetime import datetime
from sqlalchemy import String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class OrganizationProfile(Base):
    __tablename__ = "ngo_profiles"  # keep name as per your schema

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"), unique=True, nullable=False
    )

    organization_name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text)
    contact_email: Mapped[str] = mapped_column(String)
    phone_number: Mapped[str]
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    profile_image_url: Mapped[str | None]

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    user = relationship("User", back_populates="organization_profile")
    opportunities = relationship(
        "Opportunity", back_populates="organization"
    )
    images = relationship(
        "OrganizationImage", back_populates="organization"
    )