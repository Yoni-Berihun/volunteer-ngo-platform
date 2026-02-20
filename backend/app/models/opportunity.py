from sqlalchemy import String, Text, Boolean, Date, Time, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.core.database import Base
import uuid

class Opportunity(Base):
    __tablename__ = "opportunities"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    organization_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organization_profiles.id"))

    title: Mapped[str]
    description: Mapped[str] = mapped_column(Text)
    required_skills: Mapped[str]
    location: Mapped[str]
    start_date: Mapped[str]
    end_date: Mapped[str]
    start_time: Mapped[str]

    image_url: Mapped[str | None]  # default image if not provided
    has_certificate: Mapped[bool] = mapped_column(Boolean, default=False)
    has_stipend: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relationships
    organization = relationship("OrganizationProfile", back_populates="opportunities")
    applications = relationship("Application", back_populates="opportunity")