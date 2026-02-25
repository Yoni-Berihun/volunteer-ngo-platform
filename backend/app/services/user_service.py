from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.services.auth_service import create_access_token, authenticate_user


class UserService:
    @staticmethod
    def register_user(db: Session, user_data: UserCreate):
        user = UserRepository.create(db, user_data)
        return user

    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return UserRepository.get_by_email(db, email)

    @staticmethod
    def authenticate(db: Session, email: str, password: str):
        user = authenticate_user(db, email, password)
        if not user:
            return None
        access_token = create_access_token(data={"sub": user.id})
        return access_token