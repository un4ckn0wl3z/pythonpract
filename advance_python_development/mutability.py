friends_last_seen = {
    'Anuwat': 31,
    'Pansa': 1,
    'Surachad': 7
}

print(id(friends_last_seen))

friends_last_seen = {
    'Anuwat': 31,
    'Pansa': 1,
    'Surachad': 7
}

print(id(friends_last_seen))
friends_last_seen['Pansa'] = 0 # friends_last_seen.__setitem__(self, 'Pansa')
print(id(friends_last_seen))

my_int = 5
print(id(my_int))

my_int = my_int + 1 # my_int.__add__(self, 1): return cls(self.value + 1)
print(id(my_int))


friends = ['Pansa', 'Surachad']
print(id(friends))
friends.append('Anuwat')
print(id(friends))


"""
IMMUTABLE
- integers
- floats
- strings
- tuples
"""





