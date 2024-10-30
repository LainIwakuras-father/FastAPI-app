from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import select,update,delete
from sqlalchemy.ext.asyncio import AsyncSession

from app2.api.crud import create_in_table
from app2.db.db import get_session
from app2.models.model import ItemOrm
from app2.schemas.Schemas import ItemWrite, ItemRead, ItemUpdate

item_router = APIRouter(prefix="/Item", tags=["Items"])

@item_router.post("/ItemAdd")
async def todo_post(item: ItemWrite,session: AsyncSession = Depends(get_session))->ItemRead:
    stmt = await create_in_table(ItemOrm,item,session)
    return stmt


@item_router.put('/updateItem', status_code=status.HTTP_201_CREATED)
async def update_item(id:int, item: ItemUpdate,session: AsyncSession = Depends(get_session)):
    stmt = select(ItemOrm).where(ItemOrm.id == id)
    result = await session.execute(stmt)
    product = result.scalar_one_or_none()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    stmt = update(ItemOrm).where(ItemOrm.id == id).values(**item.model_dump())

    await session.execute(stmt)
    await session.commit()
    return "Success"

@item_router.delete('/deleteItem', status_code=status.HTTP_201_CREATED)
async def delete_item(id:int,session:AsyncSession = Depends(get_session)):
    stmt = delete(ItemOrm).where(ItemOrm.id==id).returning()
    await session.execute(stmt)
    await session.commit()
    return  "Success"


