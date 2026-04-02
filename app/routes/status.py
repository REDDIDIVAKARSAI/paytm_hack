from fastapi import APIRouter, Depends
from app.database import SessionLocal
from app.models import Bill

router = APIRouter()

@router.get("/status/{bill_id}")
def status(bill_id: int, db=Depends(SessionLocal)):
    bill = db.query(Bill).filter(Bill.id == bill_id).first()
    return {"status": bill.status}