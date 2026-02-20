from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.core.database import Base
import uuid

class Application(Base):
    __tablename__ = "applications"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    volunteer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("volunteer_profiles.id"))
    opportunity_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("opportunities.id"))

    status: Mapped[str] = mapped_column(default="PENDING")
    applied_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relationships
    volunteer = relationship("VolunteerProfile", back_populates="applications")
    opportunity = relationship("Opportunity", back_populates="applications")