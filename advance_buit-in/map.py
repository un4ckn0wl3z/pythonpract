friends = ['Anuwat', 'Pansa', 'Surachad', 'Chatirot', 'Pennapa']
start_with_p = filter(lambda friend: friend.startswith('P'), friends)  # lambda version
another_start_with_p = (x for x in friends if x.startswith('P'))

# friends_lower = map(lambda friend: friend.lower(), friends)
# friends_lower = [friend.lower() for friend in friends]
friends_lower = (friend.lower() for friend in friends)

print(next(friends_lower))
print(next(friends_lower))
print(next(friends_lower))
print(next(friends_lower))
print(next(friends_lower))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


users = [
    {"username": 'un4', "password": "123456"},
    {"username": 'skidcoder', "password": "haxme"}
]

users = [User.from_dict(user) for user in users]
users = map(User.from_dict, users)

print(users)
