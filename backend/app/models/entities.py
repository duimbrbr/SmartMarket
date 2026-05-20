from sqlalchemy import String, DateTime, Numeric, ForeignKey, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db.session import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    name: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String)
    categoria: Mapped[str] = mapped_column(String)
    gtin: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Purchase(Base):
    __tablename__ = "purchases"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    store_name: Mapped[str] = mapped_column(String)
    purchased_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    total: Mapped[float] = mapped_column(Numeric(10,2))
    items = relationship("PurchaseItem", back_populates="purchase", cascade="all, delete-orphan")

class PurchaseItem(Base):
    __tablename__ = "purchase_items"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    purchase_id: Mapped[int] = mapped_column(ForeignKey("purchases.id"))
    product_name: Mapped[str] = mapped_column(String)
    quantity: Mapped[float] = mapped_column(Numeric(10,3))
    unit_price: Mapped[float] = mapped_column(Numeric(10,2))
    total_price: Mapped[float] = mapped_column(Numeric(10,2))
    purchase = relationship("Purchase", back_populates="items")
