from pydantic import BaseModel
from datetime import datetime


class ApplicationCreate(BaseModel):
    opportunity_id: int


class ApplicationRead(BaseModel):
    id: int
    volunteer_id: int
    opportunity_id: int
    status: str
    applied_at: datetime
    created_at: datetime

    class Config:
        from_attributes = True