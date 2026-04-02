from fastapi import APIRouter, Depends
from app.database import SessionLocal
from app.services.billing import create_bill
from app.services.qr import generate_qr

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/bill")
def create(data: dict, db=Depends(get_db)):
    bill = create_bill(db, data)
    qr = generate_qr(bill)
    return {"bill_id": bill.id, "qr": qr}