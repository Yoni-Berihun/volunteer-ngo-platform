from sqlalchemy.orm import Session
from app.repositories.organization_repository import OrganizationRepository
from app.schemas.organization_profile import OrganizationProfileCreate


class OrganizationService:
    @staticmethod
    def create_organization(db: Session, user_id: int, data: OrganizationProfileCreate):
        organization = OrganizationRepository.create(db, user_id, data)
        return organization

    @staticmethod
    def get_organization_by_user(db: Session, user_id: int):
        return OrganizationRepository.get_by_user_id(db, user_id)