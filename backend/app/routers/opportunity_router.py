from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.opportunity import OpportunityCreate
from app.services.opportunity_service import OpportunityService
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/opportunities", tags=["Opportunities"])


@router.post("/")
def create_opportunity(
    data: OpportunityCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if current_user.role != "ORGANIZATION":
        raise HTTPException(status_code=403, detail="Only organizations can post")

    return OpportunityService.create_opportunity(db, current_user.id, data)


@router.get("/")
def list_opportunities(db: Session = Depends(get_db)):
    return OpportunityService.list_opportunities(db)