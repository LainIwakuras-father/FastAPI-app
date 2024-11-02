from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.db import Base



class ItemOrm(Base):
    __tablename__ = 'item'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    color: Mapped[str]
    amount: Mapped[int]
    user_id: Mapped[int]=mapped_column(ForeignKey("user.id",ondelete='CASCADE'))

    user:Mapped['UserOrm'] = relationship("UserOrm",back_populates='items')