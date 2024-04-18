def cart_igognito(user: str) -> str:
    return user[0:4] + " " + user[4:6] + "**" + " " + "****" + " " + user[12:16]


def bank_balance_igognito(user: str) -> str:
    return "**" + user[12:16]

__all__ = ['cart_igognito', 'bank_balance_igognito']
