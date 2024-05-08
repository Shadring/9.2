def check(user: list, key: str = " EXECUTED") -> list:
    """функция которая принимает на вход список словарей и значение для ключа state и возращает новый
    список, содержащий только те словари, у которых ключ state соедрежит переданое в функцию значение"""
    asd = []
    for i in user:
        if i["state"] == key:
            asd.append(i)
    return asd
