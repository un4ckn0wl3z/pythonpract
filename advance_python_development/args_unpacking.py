accounts = {
    'Checking': 5461.21,
    'Savings': 3642.32
}


def add_balance(amount: float, name: str = 'Checking') -> float:
    """ update balance """
    accounts[name] += amount
    return accounts[name]


transactions = [
    (-180.65, 'Checking'),
    (632.65, 'Savings'),
    (-562.65, 'Checking'),
    (62.65, 'Checking'),
    (-551.65, 'Savings'),
    (1633.65, 'Savings'),
    (-51.65, 'Checking'),
    (55.65, 'Savings'),
    (85.65, 'Checking'),
    (-51.65, 'Savings'),
    (-10.65, 'Checking'),
]

for t in transactions:
    # print(add_balance[0], t[1])) -> normal
    # print(add_balance(*t)) - unpack
    # amount, name = t -> unpack
    print(add_balance(amount=t[0], name=t[1]))  # -> specific args name


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<user>username: {self.username}, password: {self.password}</user>'

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


users = [
    {"username": 'un4', "password": "123456"},
    {"username": 'skidcoder', "password": "haxme"}
]

# users = [User.from_dict(user) for user in users]
# users = map(User.from_dict, users)
# users = [User(username=data['username'], password=data['password']) for data in users]
users = [User(**data) for data in users]
print(users)

users = [
    ('anuwat', '132456'),
    ('un4', 'dsadsad')
]

users = [User(*data) for data in users]
print(users)