from fastapi import FastAPI

from app2.api.router import all_routers

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await delete_database()
#     print("База очищена")
#     await create_database()
#     print("База готова к работе")
#     yield
#     print("Выключение")

app = FastAPI()

for router in all_routers:
    app.include_router(router)


"""
Функции ЭндПоинты!
 в роутерах
"""
# @app.put("/user{worker_id}.items/{id}", response_model=ItemRead)
# async def user_put(
#     uid: int, user_id:int,item: ItemWrite, session: AsyncSession = Depends(get_session)) -> ItemRead:
#     query = select(ItemOrm).where(ItemOrm.user_id == user_id)
#     stmt = (
#         update(query).
#         values(item.model_dump(exclude_unset=True)).
#         where(query.id==uid)
#     )
#     result = await session.execute(stmt)
#     item1 = result
#     if not item1:
#         raise HTTPException(404, "Record not found!")
#     await session.commit()
#     return item1


# @app.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
# async def user_delete(uid: int, session: AsyncSession = Depends(get_session)):
#     item = await session.execute(
#         delete(UserOrm).where(UserOrm.id == uid).returning(UserOrm.id),
#         execution_options={"synchronize_session": False},
#     )
#     if not item.scalar():
#         raise HTTPException(404, "Not found!")
#     await session.commit()
#     return  'Success'

"""
классическая функция для запуска
"""
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

