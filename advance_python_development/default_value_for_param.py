accounts = {
    'Checking': 5461.21,
    'Saving': 3642.32
}


def add_balance(amount: float, name: str = 'Checking') -> float:
    """ update balance """

    accounts[name] += amount
    return accounts[name]


add_balance(500.00)
print(accounts['Checking'])