from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.organization_service import OrganizationService

router = APIRouter(prefix="/organizations", tags=["Organizations"])


@router.get("/{user_id}")
def get_organization(user_id: int, db: Session = Depends(get_db)):
    return OrganizationService.get_organization_by_user(db, user_id)