from sqlalchemy.orm import Session
from app.models.opportunity import Opportunity
from app.schemas.opportunity import OpportunityCreate


class OpportunityRepository:

    @staticmethod
    def create(db: Session, ngo_id: int, data: OpportunityCreate):
        opportunity = Opportunity(
            ngo_id=ngo_id,
            title=data.title,
            description=data.description,
            required_skills=data.required_skills,
            location=data.location,
            start_date=data.start_date,
            end_date=data.end_date,
            start_time=data.start_time,
            has_certificate=data.has_certificate,
            has_stipend=data.has_stipend,
            image_url=data.image_url
        )

        db.add(opportunity)
        db.commit()
        db.refresh(opportunity)
        return opportunity

    @staticmethod
    def list_by_ngo(db: Session, ngo_id: int):
        return db.query(Opportunity).filter(
            Opportunity.ngo_id == ngo_id
        ).all()

    @staticmethod
    def get_by_id(db: Session, opportunity_id: int):
        return db.query(Opportunity).filter(
            Opportunity.id == opportunity_id
        ).first()