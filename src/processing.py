def state_checker(input: dict, correct: str) -> dict:
    """возрашает список только тех словарей в которых есть второе слово"""
    a = []
    for i in input:
        if i["state"] == correct:
            a.append(i)
    return a


def sort_data(input: list, valu: str) -> list:
    """сортирует и возрашает список словарей по возрастание либо по убиванию взамисимости от второго слово up либо down"""
    if valu == "down":
        sorted_data = sorted(input, key=lambda x: (x['date']))
    if valu == "up":
        sorted_data = sorted(input, key=lambda x: (x['date']), reverse=True)
    return sorted_data