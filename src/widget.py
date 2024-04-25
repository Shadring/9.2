from src.masks import account_number, card_number


def cart_or_check(user1: str) -> str:
    """указывает какую функцию надо использовать cart или check и выполняет ее"""

    if user1[0:4] == "Счет":
        return "Счет " + account_number(user1[-16:])

    else:
        return user1[:-16] + card_number(user1[-16:])


def time_formator(time: str) -> str:
    """форматирует время в формате 11.07.2018"""
    return time[8:10] + "." + time[5:7] + "." + time[0:4]
