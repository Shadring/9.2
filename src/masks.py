def card_number(user: str) -> str:
    """возрашает номер в формате xxxx xx** **** XXXX"""
    return user[:-20] + user[-20:][0:5] + user[-20:][5:8] + "**" + " ****" + user[-20:][15:20]


def account_number(user: str) -> str:
    """получает счет пользователя позврашает 6 последних цифры 2 первые в виде звезды"""
    return user[:4] + " **" + user[-4:]
