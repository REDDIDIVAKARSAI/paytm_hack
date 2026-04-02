from app.models import Payment
from datetime import datetime

def create_payment(db, amount: int):
    payment = Payment(
        amount=amount,
        source="upi",
        timestamp=datetime.utcnow()
    )
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment