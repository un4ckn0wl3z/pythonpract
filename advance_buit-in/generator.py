def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1


g = hundred_numbers()
print(next(g))
print(next(g))

my_range_object = range(10)
print(my_range_object)
print(list(g))

