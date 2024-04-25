def card_number(user: str) -> str:
    """возрашает номер в формате xxxx xx** **** XXXX"""
    return user[0:4] + " " + user[4:6] + "**" + " " + "****" + " " + user[12:16]


def account_number(user: str) -> str:
    """получает счет пользователя позврашает 6 последних цифры 2 первые в виде звезды"""
    return "**" + user[12:16]
''