from app.models import Bill

def calculate_score(payment, bill):
    score = 0

    diff = abs(payment.amount - bill.total)

    if diff == 0:
        score += 70
    elif diff <= 2:
        score += 50

    time_gap = (payment.timestamp - bill.created_at).seconds

    if time_gap < 120:
        score += 20
    elif time_gap < 300:
        score += 10

    return score


def match_payment(db, payment):
    bills = db.query(Bill).filter(Bill.status == "pending").all()

    best = None
    best_score = -1

    for bill in bills:
        score = calculate_score(payment, bill)
        if score > best_score:
            best_score = score
            best = bill

    if best_score >= 60:
        return best, best_score

    return None, 0