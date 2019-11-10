friends = ['Anuwat', 'Pansa', 'Surachad', 'Chatirot', 'Pennapa']
# print(f'My top 1 friend is {friends[0]}.')
# print(f'My top 2 friend is {friends[1]}.')
# print(f'My top 3 friend is {friends[2]}.')

for i, friend in enumerate(friends):
    print(f'My top {i + 1} friend is {friend}.')

# for friend in friends:
#     print(f'{friend} is my top friends')

friends_g = enumerate(friends)
k, v = next(friends_g)
print(k)
print(v)

