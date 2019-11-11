# mmu

friends_last_seen = {
    'Anuwat': 31,
    'Pansa': 1,
    'Surachad': 7
}


def see_friend(friends, name):
    print(friends == friends_last_seen)
    print(friends is friends_last_seen)

    print(id(friends))
    friends[name] = 0


print(id(friends_last_seen))
print(id(friends_last_seen['Pansa']))
see_friend(friends_last_seen, 'Pansa')
print(id(friends_last_seen['Pansa']))
print(id(friends_last_seen))
print(friends_last_seen['Pansa'])

# immu

age = 20

print('age[1] id:? ' , id(age))
def increase_age(current_age):
    current_age = current_age + 1
    print('current_age id:? ' , id(current_age))
    print('current_age is :? ' , current_age)


increase_age(age)
print('age[2] id:? ' , id(age))
print('age is:? ' , age)


primes = [2, 3, 5]
print('primes id:? ', id(primes))
primes += [7, 11] # modify same object
primes = primes + [7, 11] # new object
print('primes id:? ', id (primes))
