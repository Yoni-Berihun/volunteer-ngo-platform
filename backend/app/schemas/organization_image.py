from pydantic import BaseModel
from datetime import datetime


class OrganizationImageCreate(BaseModel):
    image_url: str


class OrganizationImageRead(BaseModel):
    id: int
    ngo_id: int
    image_url: str
    created_at: datetime

    class Config:
        from_attributes = True