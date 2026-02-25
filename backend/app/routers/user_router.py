from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.volunteer_profile import VolunteerProfileCreate
from app.schemas.organization_profile import OrganizationProfileCreate
from app.services.volunteer_service import VolunteerService
from app.services.organization_service import OrganizationService
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/volunteer/profile")
def create_volunteer_profile(
    data: VolunteerProfileCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if current_user.role != "VOLUNTEER":
        raise HTTPException(status_code=403, detail="Not a volunteer")

    return VolunteerService.create_profile(db, current_user.id, data)


@router.post("/organization/profile")
def create_organization_profile(
    data: OrganizationProfileCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if current_user.role != "ORGANIZATION":
        raise HTTPException(status_code=403, detail="Not an organization")

    return OrganizationService.create_organization(db, current_user.id, data)