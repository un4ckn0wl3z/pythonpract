# def greet():
#     friend = yield
#     print(f'Hello, {friend}')
#
#
# g = greet()
# g.send(None)  # priming the generator
# g.send('Anuwat')


from collections import deque
from types import coroutine

friends = deque(('Anuwat', 'Pansa', 'Surachad', 'Chatirot', 'Chonlathi'))


@coroutine
def friends_upper():  # co-routine
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print('Starting...')
    await g
    print('Ending...')


greeter = greet(friends_upper())
greeter.send(None)
greeter.send('Hello')

greeting = input('Enter greeting: ')
greeter.send(greeting)

greeting = input('Enter greeting: ')
greeter.send(greeting)