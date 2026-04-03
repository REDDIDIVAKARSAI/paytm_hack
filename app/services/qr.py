import qrcode

def generate_qr(bill):
    merchant_upi = "yourupi@okaxis"
    merchant_name = "Divakar Store"

    # 🔥 Extract ONLY item names (remove quantity)
    raw_items = bill.items.split(",")

    item_names = []
    for item in raw_items:
        parts = item.strip().split(" ")
        
        # remove quantity (first token)
        if parts[0].isdigit():
            name = " ".join(parts[1:])
        else:
            name = item
        
        item_names.append(name)

    # join items
    items_str = ",".join(item_names)

    # ⚠️ keep it short (UPI limit safety)
    if len(items_str) > 50:
        items_str = items_str[:50]

    upi_link = (
        f"upi://pay?"
        f"pa={merchant_upi}"
        f"&pn={merchant_name}"
        f"&am={bill.total}"
        f"&cu=INR"
        f"&tn={items_str}"
    )

    import base64
    from io import BytesIO
    img = qrcode.make(upi_link)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()
