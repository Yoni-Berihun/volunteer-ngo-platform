from fastapi import FastAPI
from app.core.database import engine, Base
from app.models import user, volunteer_profile, organizational_profile, opportunity, application
Base.metadata.create_all(bind=engine)
from app.routers import (
    auth_router,
    user_router,
    organization_router,
    opportunity_router,
    application_router
)

app = FastAPI(title="Volunteer & Organization Platform")

app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(organization_router.router)
app.include_router(opportunity_router.router)
app.include_router(application_router.router)