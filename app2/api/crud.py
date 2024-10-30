from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app2.db.db import get_session



async def create_in_table(model, schema, session):
    para = model(**schema.model_dump())
    session.add(para)
    await session.commit()
    await session.refresh(para)
    return para


async def read_in_table():
       pass

async def update_in_table():
        pass
async  def delete_in_table():
        pass