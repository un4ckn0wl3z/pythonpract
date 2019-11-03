class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car{self.make} {self.model}>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Try to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects.')
        self.cars.append(car)


car = Garage()
ford = Car('Ford', 'Fiesta')

try:
    car.add_car(ford)
except TypeError:
    print('Your car was not a Car!')
except ValueError:
    print('Something weired happened...')
finally:
    print(f'The garage now has {len(car)} cars.')
