class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grade = new_grade

    def average(self):
        return sum(self.grade) / len(self.grade)


student_one = Student('Anuwat', [70, 80, 90, 99]);
print(student_one.name)
print(student_one.grade)
print(student_one.average())


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

    def __repr__(self):
        return f'<Garage {self.cars}>'

    def __str__(self):
        return f'<Garage with {len(self)} cars>'


ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(len(ford))
print(ford[0])
print(ford)

for car in ford:
    print(car)
