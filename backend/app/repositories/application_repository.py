from sqlalchemy.orm import Session
from app.models.application import Application


class ApplicationRepository:

    @staticmethod
    def create(db: Session, volunteer_id: int, opportunity_id: int):
        application = Application(
            volunteer_id=volunteer_id,
            opportunity_id=opportunity_id,
            status="PENDING"
        )

        db.add(application)
        db.commit()
        db.refresh(application)
        return application

    @staticmethod
    def list_by_volunteer(db: Session, volunteer_id: int):
        return db.query(Application).filter(
            Application.volunteer_id == volunteer_id
        ).all()

    @staticmethod
    def list_by_opportunity(db: Session, opportunity_id: int):
        return db.query(Application).filter(
            Application.opportunity_id == opportunity_id
        ).all()