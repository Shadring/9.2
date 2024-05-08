def check(user: list, key: str = " EXECUTED") -> list:
    asd = []
    for i in user:
        if i["state"] == key:
            asd.append(i)
    return asd
