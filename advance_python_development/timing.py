import time
import timeit


def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)


def powers(limit):
    return [x ** 2 for x in range(limit)]


# measure_runtime(powers)

measure_runtime(lambda: powers(5000))

print(timeit.timeit("[x ** 2 for x in range(10)]"))