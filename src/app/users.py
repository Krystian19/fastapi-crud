from fastapi import APIRouter, Path
from typing import List, Optional 
from datetime import datetime as dt

from app.models import UserDB, UserSchema, UserFieldsSchema
from app import crud

router = APIRouter()

@router.get("/v1/users", response_model=List[UserDB])
async def get_all_users():
    return await crud.get_users()

@router.get("/v1/users/{user_id}", response_model=Optional[UserDB])
async def get_user(user_id: int = Path(..., gt=0)):
    return await crud.get_user(id=user_id)

@router.post("/v1/users", response_model=UserDB, status_code=201)
async def create_user(payload: UserSchema):
    created_user_id = await crud.create_user(payload=payload)

    return await crud.get_user(created_user_id)

@router.put("/v1/users/{user_id}", response_model=Optional[UserDB], status_code=202)
async def update_user(user_id:int, payload: UserFieldsSchema):
        found_user = await crud.get_user(id=user_id)

        if not found_user:
            return None

        await crud.update_user(found_user.id, payload=payload)
        return await crud.get_user(found_user.id)

@router.delete("/v1/users/{user_id}", response_model=Optional[UserDB])
async def destroy_user(user_id: int = Path(...,gt=0)):
    found_user = await crud.get_user(id=user_id)

    if not found_user:
        return None

    await crud.destroy_user(found_user.id)
    return found_user
