from fastapi import FastAPI

from .database import engine
from .models import Base
from .routes import users, posts, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(posts.router)