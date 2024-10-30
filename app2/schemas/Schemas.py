"""СХЕМЫ ДЛЯ PYDANTIC VALIDATION"""
from pydantic import BaseModel

class ItemUpdate(BaseModel):
    name:str
    color:str
    amount:int

class ItemWrite(ItemUpdate):
    user_id:int

class ItemRead(ItemWrite):
    id:int

class UserWrite(BaseModel):
    name:str
    surname: str
    age: int

class UserRead(UserWrite):
    id: int

class ItemRel(ItemRead):
    user: "UserRead"

class UserRel(UserRead):
    items: list["ItemRead"]
