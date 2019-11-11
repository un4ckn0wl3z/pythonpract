# def create_account(name: str, holder: str, account_holder: list = []):
def create_account(name: str, holder: str, account_holder = None):
    print(id(account_holder))
    if not account_holder:
        account_holder = []

    account_holder.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holder
    }


a1 = create_account('checking', 'Anuwat')
a2 = create_account('checking', 'Surachad')
a3 = create_account('saving', 'Pansa', ['Chatirot', 'Thanasit'])
print(a1)
print(a2)
print(a3)