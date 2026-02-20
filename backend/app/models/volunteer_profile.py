from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
import uuid

class VolunteerProfile(Base):
    __tablename__ = "volunteer_profiles"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), unique=True)

    full_name: Mapped[str]
    skills: Mapped[str]  # JSON string
    interests: Mapped[str]
    availability: Mapped[str]
    location: Mapped[str]
    profile_image_url: Mapped[str | None]
    phone_number: Mapped[str]

    # Relationships
    user = relationship("User", back_populates="volunteer_profile")
    applications = relationship("Application", back_populates="volunteer")