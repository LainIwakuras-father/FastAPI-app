from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app2.db.db import Base


class UserOrm(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname:Mapped[str]
    age: Mapped[int]
    items:Mapped[list['ItemOrm']]=relationship(back_populates='user')

class ItemOrm(Base):
    __tablename__ = 'item'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    color: Mapped[str]
    amount: Mapped[int]
    user_id: Mapped[int]=mapped_column(ForeignKey("user.id",ondelete='CASCADE'))
    user:Mapped['UserOrm'] = relationship(back_populates='items')
