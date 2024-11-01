from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from app_lifecode.db.db import Base

class UserOrm(Base):
    __tablename__='user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    age: Mapped[str]
    order: Mapped['OrderOrm']=relationship('OrderOrm',back_populates='user')


class OrderOrm(Base):
    __tablename__='orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]=mapped_column(ForeignKey("user.id",ondelete='CASCADE'))
    status: Mapped[str]
    product: Mapped[list['Product_OrderOrm']]=relationship('Product_OrderOrm',back_population='orders')


class Product_OrderOrm(Base):
    __tablename__='product_order'
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id:  Mapped[int]=mapped_column(ForeignKey("orders.id",ondelete='CASCADE'))
    Product_id: Mapped[int]=mapped_column(ForeignKey("product.id",ondelete='CASCADE'))
    count:Mapped[int]

    order: Mapped["OrderOrm"] = relationship("OrderOrm", back_populates="product_order")
    product: Mapped["ProductOrm"] = relationship("ProductOrm", back_populates="product_order")


class ProductOrm(Base):
    __tablename__='product'
    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    price:Mapped[str]
    count:Mapped[str]
    product_order:Mapped['Product_OrderOrm']=relationship(Product_OrderOrm, back_populates='product')


