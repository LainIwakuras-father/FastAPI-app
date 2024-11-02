from app.schemas.item_schema import ItemRead
from app.schemas.user_schema import UserRead


class ItemRel(ItemRead):
    user: "UserRead"

class UserRel(UserRead):
    items: list["ItemRead"]
