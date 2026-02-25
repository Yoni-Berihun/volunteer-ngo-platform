import uuid
from datetime import datetime
from sqlalchemy import String, Text, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class VolunteerProfile(Base):
    __tablename__ = "volunteer_profiles"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"), unique=True, nullable=False
    )

    full_name: Mapped[str] = mapped_column(String, nullable=False)
    skills: Mapped[str] = mapped_column(Text)
    interests: Mapped[str] = mapped_column(Text)
    availability: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    profile_image_url: Mapped[str | None]
    phone_number: Mapped[str]

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    user = relationship("User", back_populates="volunteer_profile")
    applications = relationship(
        "Application", back_populates="volunteer"
    )