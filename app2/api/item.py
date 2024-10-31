from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app2.api.crud import create_in_table, update_in_table, delete_in_table
from app2.db.db import get_session
from app2.models.model import ItemOrm
from app2.schemas.Schemas import ItemWrite, ItemRead, ItemUpdate

item_router = APIRouter(prefix="/Item", tags=["Items"])

@item_router.post("/ItemAdd")
async def todo_post(item: ItemWrite,session: AsyncSession = Depends(get_session))->ItemRead:
    return await create_in_table(ItemOrm, item, session)


@item_router.put('/updateItem', status_code=status.HTTP_201_CREATED)
async def update_item(id:int, item: ItemUpdate,session: AsyncSession = Depends(get_session)):
    return await update_in_table(id,ItemOrm,item,session)


@item_router.delete('/deleteItem', status_code=status.HTTP_201_CREATED)
async def delete_item(id:int,session:AsyncSession = Depends(get_session)):
    return await delete_in_table(id,ItemOrm,session)


