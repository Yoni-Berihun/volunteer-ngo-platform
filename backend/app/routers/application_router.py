from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.application_service import ApplicationService
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/applications", tags=["Applications"])


@router.post("/{opportunity_id}")
def apply(
    opportunity_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if current_user.role != "VOLUNTEER":
        raise HTTPException(status_code=403, detail="Only volunteers can apply")

    return ApplicationService.apply_to_opportunity(
        db, current_user.id, opportunity_id
    )