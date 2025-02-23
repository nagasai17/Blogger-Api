from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models, schemas, auth
from database import get_db
from exceptions import raise_unauthorized_exception

from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from typing import Annotated

router = APIRouter(
    tags=["auth"],
)

db_dependency = Annotated[Session, Depends(get_db)]

# Login Endpoint
@router.post("/token", response_model=schemas.Token)
def login_for_access_token(
    db: db_dependency, form_data: OAuth2PasswordRequestForm = Depends()
):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise_unauthorized_exception("Incorrect username or password")
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}