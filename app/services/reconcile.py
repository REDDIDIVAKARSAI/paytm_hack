from app.models import Match

def reconcile(db, bill, payment, score):
    bill.status = "paid"

    match = Match(
        bill_id=bill.id,
        payment_id=payment.id,
        score=score
    )

    db.add(match)
    db.commit()

    return {"status": "matched", "confidence": score}