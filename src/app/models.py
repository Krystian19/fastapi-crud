from pydantic import BaseModel, Field
from datetime import datetime as dt

class UserFieldsSchema(BaseModel):
    email: str = Field(..., min_length=5, max_length=40) 
    username: str = Field(..., min_length=3, max_length=35) 

class UserSchema(UserFieldsSchema):
    created_at: str = dt.now().strftime("%Y-%m-%d %H:%M")

class UserDB(UserSchema):
    id: int
