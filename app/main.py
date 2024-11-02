from fastapi import FastAPI

from app.api.router import all_routers

app = FastAPI()

for router in all_routers:
    app.include_router(router)

"""
классическая функция для запуска
"""
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

