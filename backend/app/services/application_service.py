from sqlalchemy.orm import Session
from app.repositories.application_repository import ApplicationRepository
from app.schemas.applicaiton import ApplicationCreate                                                                                    


class ApplicationService:
    @staticmethod
    def apply_to_opportunity(db: Session, volunteer_id: int, opportunity_id: int):
        application = ApplicationRepository.create(db, volunteer_id, opportunity_id)
        return application

    @staticmethod
    def get_applications_by_volunteer(db: Session, volunteer_id: int):
        return ApplicationRepository.list_by_volunteer(db, volunteer_id)

    @staticmethod
    def get_applications_by_opportunity(db: Session, opportunity_id: int):
        return ApplicationRepository.list_by_opportunity(db, opportunity_id)