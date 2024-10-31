from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status

from app2.api.crud import create_in_table, delete_in_table, read_in_table_user_id, read_in_table_user
from app2.db.db import get_session
from app2.models.model import UserOrm
from app2.schemas.Schemas import UserRead, UserRel, UserWrite

user_router=APIRouter(prefix='/users',tags=['users'])

@user_router.get("")
async def users_read(session: AsyncSession = Depends(get_session)):
     return await read_in_table_user(session)


@user_router.post("/userAdd" , response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def user_create(
    user: UserWrite, session: AsyncSession = Depends(get_session)) -> UserRead:
    return await create_in_table(UserOrm,user,session)


@user_router.get("/{id}")
async def user_read(id: int, session: AsyncSession = Depends(get_session)) ->UserRel:
    return await read_in_table_user_id(id,session)


@user_router.delete('/deleteUser', status_code=status.HTTP_201_CREATED)
async def delete_user(id:int,session:AsyncSession = Depends(get_session)):
    return await delete_in_table(id,UserOrm,session)