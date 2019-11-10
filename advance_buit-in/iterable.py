class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self


class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]


for car in AnotherIterable():
    print(car)

# tips for Generator

my_numbers = [x for x in [1,2,3,4,5]] # lists
my_numbers_gen = (x for x in [1,2,3,4,5]) # Generator

print(my_numbers)
print(next(my_numbers_gen))
print(next(my_numbers_gen))
print(next(my_numbers_gen))

