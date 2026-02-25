from sqlalchemy.orm import Session
from app.models.volunteer_profile import VolunteerProfile
from app.schemas.volunteer_profile import VolunteerProfileCreate


class VolunteerRepository:

    @staticmethod
    def create(db: Session, user_id: int, data: VolunteerProfileCreate):
        profile = VolunteerProfile(
            user_id=user_id,
            full_name=data.full_name,
            skills=data.skills,
            interests=data.interests,
            availability=data.availability,
            location=data.location,
            phone_number=data.phone_number,
            profile_image_url=data.profile_image_url
        )

        db.add(profile)
        db.commit()
        db.refresh(profile)
        return profile

    @staticmethod
    def get_by_user_id(db: Session, user_id: int):
        return db.query(VolunteerProfile).filter(
            VolunteerProfile.user_id == user_id
        ).first()