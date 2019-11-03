class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    @property
    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 37.5


anuwat = WorkingStudent('Anuwat', 'RMUTSV', 15.50)
print(anuwat.salary)
anuwat.marks.append(57)
anuwat.marks.append(99)
print(anuwat.average)

print(anuwat.weekly_salary)

pansa = Student('Pansa', 'Oxford')
print(f"{pansa.name} - {pansa.school}")

