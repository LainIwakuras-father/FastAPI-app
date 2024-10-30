from app2.api.User import user_router
from app2.api.item import item_router
from app2.api.work_db import db_router

all_routers = [
    item_router,
    user_router,
    db_router
]