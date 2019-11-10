def starts_with_p(friend):
    return friend.startswith('P')


friends = ['Anuwat', 'Pansa', 'Surachad', 'Chatirot', 'Pennapa']
# start_with_p = filter(starts_with_p, friends) # arg1: return True or False
# start_with_p = filter(lambda friend: friend.startswith('P'), friends)  # lambda version
another_start_with_p = (x for x in friends if x.startswith('P'))


def custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


start_with_p = custom_filter(lambda friend: friend.startswith('P'), friends)  # custom filter

print(next(start_with_p))
print(list(start_with_p))
