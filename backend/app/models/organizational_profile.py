from sqlalchemy import String, Text, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
import uuid

class OrganizationProfile(Base):
    __tablename__ = "organization_profiles"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), unique=True)

    organization_name: Mapped[str]
    description: Mapped[str] = mapped_column(Text)
    contact_email: Mapped[str]
    phone_number: Mapped[str]
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    profile_image_url: Mapped[str | None]

    # Relationships
    user = relationship("User", back_populates="organization_profile")
    opportunities = relationship("Opportunity", back_populates="organization")
    images = relationship("OrganizationImage", back_populates="organization")