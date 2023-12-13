from app.db import users, database
from app.models import UserSchema
from datetime import datetime as dt

async def get_user(id: int):
    query = users.select().where(id == users.c.id)
    return await database.fetch_one(query=query)

async def get_users():
    query = users.select()
    return await database.fetch_all(query=query)

async def create_user(payload: UserSchema):
    query = users.insert().values(email=payload.email, username=payload.username, created_at=dt.now().strftime("%Y-%m-%d %H:%M"))
    return await database.execute(query=query)

async def destroy_user(id: int):
    query = users.delete().where(id == users.c.id)
    return await database.execute(query=query)
