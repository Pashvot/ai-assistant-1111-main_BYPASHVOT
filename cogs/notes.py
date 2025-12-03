import os
from cogs.constants import NAME


def add_note(text):
    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")
    return f"{NAME}: Я записав, але міг би й запам'ятати сам."


def read_notes():
    if not os.path.exists("notes.txt"):
        return f"У тебе ще немає нотаток."

    with open("notes.txt", "r", encoding="utf-8") as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]

    if not lines:
        return "Файл є, але нотатки порожні."
    
    result = ["Твої нотатки:"]
    for i, line in enumerate(lines, 1):
        result.append(f"{i}) {line}")

    return "\n".join(result)


def clear_notes():
    with open("notes.txt", "w", encoding="utf-8") as f:
        f.write("")
    return f"{NAME}: Готово. Нотатки стерті."
