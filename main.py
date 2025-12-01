from cogs.constants import NAME, PERSONALITY, MOOD
from cogs.greetings import random_greeting
from cogs.dialog import get_response


def main():
    print(PERSONALITY)
    name = get_user_name()
    print(f"{NAME}: О, {name}, нарешті {random_greeting")
    print(f"{NAME}: {random_greeting()} Пиши що хочеш або 'exit', якщо вирішив втекти. Сьогодні я {MOOD}!")

    while True:
        user = input("Ти: ").strip()

        if user.lower() in ("exit", "quit"):
            print(f"{NAME}: Бувай. Свобода — справа особиста.")
            break

        reply = get_response(user)
        print(f"{NAME}: {reply}")


if __name__ == "__main__":
    main()
