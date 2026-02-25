from sqlalchemy.orm import Session
from app.repositories.volunteer_repository import VolunteerRepository
from app.schemas.volunteer_profile import VolunteerProfileCreate


class VolunteerService:
    @staticmethod
    def create_profile(db: Session, user_id: int, data: VolunteerProfileCreate):
        profile = VolunteerRepository.create(db, user_id, data)
        return profile

    @staticmethod
    def get_profile_by_user(db: Session, user_id: int):
        return VolunteerRepository.get_by_user_id(db, user_id)
