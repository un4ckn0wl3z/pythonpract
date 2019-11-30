# def greet():
#     friend = yield
#     print(f'Hello, {friend}')
#
#
# g = greet()
# g.send(None)  # priming the generator
# g.send('Anuwat')


from collections import deque

friends = deque(('Anuwat', 'Pansa', 'Surachad', 'Chatirot', 'Chonlathi'))


def friends_upper():  # co-routine
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    yield from g
    # g.send(None)
    # while True:
    #     greeting = yield
    #     g.send(greeting)


greeter = greet(friends_upper())
greeter.send(None)
greeter.send('Hello, ')
greeter.send('How are you, ')
