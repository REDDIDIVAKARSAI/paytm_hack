from app.models import Bill
from datetime import datetime

def create_bill(db, data):
    bill = Bill(
        items=",".join(data["items"]),
        total=data["total"],
        created_at=datetime.utcnow(),
        status="pending"
    )
    db.add(bill)
    db.commit()
    db.refresh(bill)
    return bill