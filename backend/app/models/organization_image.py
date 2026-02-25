import uuid
from datetime import datetime
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class OrganizationImage(Base):
    __tablename__ = "ngo_images"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=uuid.uuid4
    )
    ngo_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("ngo_profiles.id"), nullable=False
    )

    image_url: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    organization = relationship(
        "OrganizationProfile", back_populates="images"
    )