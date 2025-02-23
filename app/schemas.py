from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# User Schemas

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    
# allows the model to be initialized using objects 
# (or ORM-like attributes) instead of just plain dictionaries.
    class Config:
        from_attributes = True

# Token Schemas

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Post Schemas

class PostBase(BaseModel):
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    timestamp: datetime
    owner_id: int

class PostWithCounts(Post):
    likes_count: int
    retweets_count: int
    owner_username: str
    
class PostUpdate(BaseModel):
    content: str

    class Config:
        from_attributes = True

# Like Schemas (if needed)

class Like(BaseModel):
    user_id: int
    post_id: int

    class Config:
        from_attributes = True

# Retweet Schemas (if needed)

class Retweet(BaseModel):
    user_id: int
    post_id: int
    timestamp: datetime

    class Config:
        from_attributes = True