from pydantic import BaseModel
from datetime import datetime

class PurchaseItemIn(BaseModel):
    product_name: str
    quantity: float
    unit_price: float
    total_price: float

class PurchaseIn(BaseModel):
    user_id: str
    store_name: str
    total: float
    items: list[PurchaseItemIn]

class PurchaseOut(PurchaseIn):
    id: int
    purchased_at: datetime
