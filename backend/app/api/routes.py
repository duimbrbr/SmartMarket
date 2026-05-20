from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.entities import Purchase, PurchaseItem, Product
from app.schemas.purchase import PurchaseIn
from app.services.ocr_parser import parse_receipt_text

router = APIRouter(prefix="/api")

@router.get('/health')
def health():
    return {"status": "ok"}

@router.get('/products')
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.post('/purchases')
def create_purchase(payload: PurchaseIn, db: Session = Depends(get_db)):
    purchase = Purchase(user_id=payload.user_id, store_name=payload.store_name, total=payload.total)
    db.add(purchase)
    db.flush()
    for item in payload.items:
        db.add(PurchaseItem(purchase_id=purchase.id, **item.model_dump()))
    db.commit()
    db.refresh(purchase)
    return purchase

@router.post('/ocr/parse')
def parse_ocr(payload: dict):
    return {"items": parse_receipt_text(payload.get("text", ""))}
