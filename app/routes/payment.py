from fastapi import APIRouter, Depends
from app.database import SessionLocal
from app.services.payment import create_payment
from app.services.matching import match_payment
from app.services.reconcile import reconcile

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/payment")
def pay(amount: int, db=Depends(get_db)):
    payment = create_payment(db, amount)

    bill, score = match_payment(db, payment)

    if bill:
        return reconcile(db, bill, payment, score)

    return {"status": "unmatched"}