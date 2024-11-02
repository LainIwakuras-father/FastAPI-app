from app.schemas.item_schema import ItemWrite, ItemUpdate
from app.utils.repository import AbstractRepository


class ItemService:
    def __init__(self, items_repo: AbstractRepository):
        self.items_repo: AbstractRepository = items_repo()

    async def add_item(self, item: ItemWrite):
        product_dict = item.model_dump()
        product_id = await self.items_repo.add_one(product_dict)
        return product_id

    async def get_items(self):
        items = await self.items_repo.find_all()
        return items

    async def update_info(self, id: int, new_data: ItemUpdate):
        result = await self.items_repo.update_info(id, new_data)
        return result

    async def delete_item(self, id):
        result = await self.items_repo.delete_item(id)
        return result