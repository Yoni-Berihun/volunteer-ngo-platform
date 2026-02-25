import uuid
from datetime import datetime
from sqlalchemy import (
    String, Text, Boolean, ForeignKey, DateTime
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class Opportunity(Base):
    __tablename__ = "opportunities"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=uuid.uuid4
    )
    ngo_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("ngo_profiles.id"), nullable=False
    )

    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text)
    required_skills: Mapped[str]
    location: Mapped[str]
    start_date: Mapped[str]
    end_date: Mapped[str]
    start_time: Mapped[str]

    image_url: Mapped[str | None]
    has_certificate: Mapped[bool] = mapped_column(Boolean, default=False)
    has_stipend: Mapped[bool] = mapped_column(Boolean, default=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    organization = relationship(
        "OrganizationProfile", back_populates="opportunities"
    )
    applications = relationship(
        "Application", back_populates="opportunity"
    )