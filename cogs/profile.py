import os
import json
from cogs.constants import NAME


def add_fact(text):
    if not os.path.exists("user.json"):
        return "Файл профілю не знайдено."

    with open("user.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    if "facts" not in data:
        data["facts"] = []

    data["facts"].append(text)

    with open("user.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return f"{NAME}: Додав. Ще один факт про тебе у моїй памʼяті."


def show_profile():
    if not os.path.exists("user.json"):
        return "Профіль не знайдено."

    with open("user.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    out = []
    if "name" in data:
        out.append(f"Ім'я: {data['name']}")
    if "favorite" in data:
        out.append(f"Улюблена тема: {data['favorite']}")
    if "level" in data:
        out.append(f"Рівень: {data['level']}")
    if "facts" in data:
        out.append("Факти про тебе:")
        for i, fact in enumerate(data["facts"], 1):
            out.append(f"  {i}) {fact}")

    return "\n".join(out) if out else "Профіль порожній."
