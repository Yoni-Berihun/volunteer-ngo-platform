from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str  # "VOLUNTEER" | "ORGANIZATION" | "ADMIN"


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserRead(BaseModel):
    id: str
    email: EmailStr
    role: str
    is_active: bool

    class Config:
        from_attributes = True