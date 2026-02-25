from sqlalchemy.orm import Session
from app.repositories.opportunity_repository import OpportunityRepository
from app.schemas.opportunity import OpportunityCreate


class OpportunityService:
    @staticmethod
    def create_opportunity(db: Session, ngo_id: int, data: OpportunityCreate):
        opportunity = OpportunityRepository.create(db, ngo_id, data)
        return opportunity

    @staticmethod
    def list_opportunities(db: Session, ngo_id: int):
        return OpportunityRepository.list_by_ngo(db, ngo_id)

    @staticmethod
    def get_opportunity(db: Session, opportunity_id: int):
        return OpportunityRepository.get_by_id(db, opportunity_id)