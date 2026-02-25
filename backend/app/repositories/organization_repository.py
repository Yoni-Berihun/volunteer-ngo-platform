from sqlalchemy.orm import Session
from app.models.organizational_profile import OrganizationProfile
from app.schemas.organization_profile import OrganizationProfileCreate


class OrganizationRepository:

    @staticmethod
    def create(db: Session, user_id: int, data: OrganizationProfileCreate):
        org = OrganizationProfile(
            user_id=user_id,
            organization_name=data.organization_name,
            description=data.description,
            contact_email=data.contact_email,
            phone_number=data.phone_number,
            profile_image_url=data.profile_image_url
        )

        db.add(org)
        db.commit()
        db.refresh(org)
        return org

    @staticmethod
    def get_by_user_id(db: Session, user_id: int):
        return db.query(OrganizationProfile).filter(
            OrganizationProfile.user_id == user_id
        ).first()