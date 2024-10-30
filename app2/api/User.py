from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from fastapi import status

from app2.api.crud import create_in_table
from app2.db.db import get_session
from app2.models.model import UserOrm
from app2.schemas.Schemas import UserRead, UserRel, UserWrite

user_router=APIRouter(prefix='/users',tags=['users'])

@user_router.get("")
async def users_read(session: AsyncSession = Depends(get_session)):
    query =(select(UserOrm)
            .options(selectinload(UserOrm.items))
            )
    res = await session.execute(query)
    return res.scalars().all()


@user_router.post("/userAdd" , response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def user_create(
    user: UserWrite, session: AsyncSession = Depends(get_session)
) -> UserRead:
    stmt = await create_in_table(UserOrm,user,session)
    return stmt


@user_router.get("/{id}")
async def user_read(id: int, session: AsyncSession = Depends(get_session)) -> UserRel:
    query = (select(UserOrm)
             .options(selectinload(UserOrm.items))
             .where(UserOrm.id == id)
             )
    res = await session.execute(query)
    return res.scalars().one_or_none()

@user_router.delete('/deleteUser', status_code=status.HTTP_201_CREATED)
async def delete_user(id:int,session:AsyncSession = Depends(get_session)):
    stmt = delete(UserOrm).where(UserOrm.id==id).returning()
    await session.execute(stmt)
    await session.commit()
    return  "Success"