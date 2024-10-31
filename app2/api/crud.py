from fastapi import HTTPException

from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app2.models.model import ItemOrm, UserOrm



async def create_in_table(model, schema, session:AsyncSession):
    para = model(**schema.model_dump())
    session.add(para)
    await session.commit()
    await session.refresh(para)
    return para


async def read_in_table_user(session:AsyncSession):
    query = (select(UserOrm)
             .options(selectinload(UserOrm.items))
             )
    res = await session.execute(query)
    if res is None:
        raise HTTPException(status_code=404, detail="Ничего не найдено!")
    return res.scalars().all()

async def read_in_table_user_id(id,session:AsyncSession):
    try:
        query = (select(UserOrm)
                 .options(selectinload(UserOrm.items))
                 .where(UserOrm.id == id)
                 )
        res = await session.execute(query)
        if res is None:
            raise HTTPException(status_code=403, detail={'message': "user not Found!"})
        return res.scalars().one_or_none()
    except:
        raise HTTPException(status_code=403, detail={'message': "user not Found!"})



async def update_in_table(id, model,schema,session:AsyncSession):
    stmt = select(model).where(ItemOrm.id == id)
    result = await session.execute(stmt)
    product = result.scalar_one_or_none()

    if product is None:
        raise HTTPException(status_code=404, detail="not found")

    stmt = update(ItemOrm).where(ItemOrm.id == id).values(**schema.model_dump())

    await session.execute(stmt)
    await session.commit()
    return "Success"


async  def delete_in_table(id,model,session:AsyncSession):
    existing_task = await session.get(model, id)
    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    await session.delete(existing_task)
    await session.commit()
    return 'Success'