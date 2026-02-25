from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class VolunteerProfileBase(BaseModel):
    full_name: str
    skills: Optional[List[str]] = []
    interests: Optional[str] = None
    availability: Optional[str] = None
    location: Optional[str] = None
    phone_number: Optional[str] = None
    profile_image_url: Optional[str] = None


class VolunteerProfileCreate(VolunteerProfileBase):
    pass


class VolunteerProfileRead(VolunteerProfileBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True