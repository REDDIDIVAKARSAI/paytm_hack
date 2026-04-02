import re

def normalize(text: str) -> str:
    text = text.replace("ek", "1").replace("do", "2")
    text = text.replace("aur", "and")
    return text

def parse_text(text: str):
    text = normalize(text)

    numbers = list(map(int, re.findall(r'\d+', text)))
    if not numbers:
        return None

    total = max(numbers)

    words = text.split()
    items = []

    for i in range(len(words) - 1):
        if words[i].isdigit():
            items.append(words[i] + " " + words[i + 1])

    return {"items": items, "total": total}