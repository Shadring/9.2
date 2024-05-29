def filter_by_currency(name: dict, valuta: str) -> dict:
    """возрашает айди карт ц которых подходяшая валюта"""
    a = []
    for i in name:
        if i["code"] == valuta:
            a.append(i["id"])
    return a


def transaction_descriptions(name: dict) -> list:
    """принимает список словарей и возвращает описание каждой операции"""
    a = []
    for i in name:
        a.append(name["description"])
    return a


def card_number_generator(start, end):
    """генератор номера карт"""
    current = start
    while current <= end:
        card_number = '{:04d} {:04d} {:04d} {:04d}'.format(current // 10**12, (current // 10**8) % 10**4,
                                                           (current // 10**4) % 10**4, current % 10**4)
        yield card_number
        current += 1

