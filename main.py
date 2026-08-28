from fastapi import FastAPI, HTTPException

from apartments.handler import apartment_app
from districts.handler import district_app
from humans.handler import humans_app


app = FastAPI(
    title="Collection Program REST API",
    description="API for managing apartments in the collection program.",
    version="1.0.0",
    docs_url="/",
)

app.include_router(apartment_app, prefix="/apartments", tags=["apartments"])
app.include_router(district_app, prefix="/districts", tags=["districts"])
app.include_router(humans_app, prefix="/humans", tags=["humans"])