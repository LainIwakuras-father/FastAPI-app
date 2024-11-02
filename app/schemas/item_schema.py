from pydantic import BaseModel


class ItemUpdate(BaseModel):
    name:str
    color:str
    amount:int

class ItemWrite(ItemUpdate):
    user_id:int

class ItemRead(ItemWrite):
    id:int