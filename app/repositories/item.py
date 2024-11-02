from app.models.item import ItemOrm
from app.utils.repository import SQLAlchemyRepository


class ItemRepository(SQLAlchemyRepository):
    model = ItemOrm