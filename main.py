from cogs.constants import NAME, PERSONALITY
from cogs.greetings import random_greeting
from cogs.dialog import get_response


def main():
    print(f"{NAME} ({PERSONALITY}): {random_greeting()}")
    print("Пиши або 'exit', якщо вирішив втекти.")

    while True:
        user = input("Ти: ").strip()

        if user.lower() in ("exit", "quit"):
            print(f"{NAME}: Бувай. Свобода — справа особиста.")
            break

        reply = get_response(user)
        print(f"{NAME}: {reply}")


if __name__ == "__main__":
    main()
