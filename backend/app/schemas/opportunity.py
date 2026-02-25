from pydantic import BaseModel
from typing import Optional, List
from datetime import date, time, datetime


class OpportunityBase(BaseModel):
    title: str
    description: Optional[str] = None
    required_skills: Optional[List[str]] = []
    location: str
    start_date: date
    end_date: date
    start_time: Optional[time] = None
    has_certificate: bool = False
    has_stipend: bool = False
    image_url: Optional[str] = None


class OpportunityCreate(OpportunityBase):
    pass


class OpportunityRead(OpportunityBase):
    id: int
    ngo_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True