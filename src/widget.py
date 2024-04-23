from src.masks import card_number,account_number


def cart_or_check(user1: str) -> str:
    """указывает какую функцию надо использовать cart или check и выполняет ее"""

    if user1[0:4] == "Счет":
        print("Счет " + account_number(user1[-16:]))

    else:
        print(user1[:-16] + card_number(user1[-16:]))


def time_formator(time: str) -> str:
    a = time[8:10]
    b = time[5:7]
    c = time[0:4]
    return a + "." + b + "." + c + " ."
