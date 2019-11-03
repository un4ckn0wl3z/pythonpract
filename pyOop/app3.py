class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


anuwat = Student('Anuwat', 'RMUTSV')
anuwat.marks.append(78)
anuwat.marks.append(99)

print(anuwat.average())


class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)


my_foo = Foo()
my_foo.hi()


class Bar:
    @staticmethod
    def hi():
        print('Hello, I don\'t take args.')

Bar.hi()
