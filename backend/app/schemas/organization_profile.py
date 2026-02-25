from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class OrganizationProfileBase(BaseModel):
    organization_name: str
    description: Optional[str] = None
    contact_email: EmailStr
    phone_number: str
    profile_image_url: Optional[str] = None


class OrganizationProfileCreate(OrganizationProfileBase):
    pass


class OrganizationProfileRead(OrganizationProfileBase):
    id: str
    user_id: str
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True