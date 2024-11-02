from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from app.api.router import all_routers
from app.exception.exception import custom_http_exception_handler, custom_requestvalueError_handler

app = FastAPI()


app.add_exception_handler(HTTPException,custom_http_exception_handler)
app.add_exception_handler(RequestValidationError,custom_requestvalueError_handler)

for router in all_routers:
    app.include_router(router)

"""
классическая функция для запуска
"""
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

