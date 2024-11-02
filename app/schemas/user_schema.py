from pydantic import BaseModel


class UserWrite(BaseModel):
    name:str
    surname: str
    age: int

class UserRead(UserWrite):
    id: int
