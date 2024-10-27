
class NameSurname:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
class Student:
    student_amount = 0
    def __init__(self,name, surname, age,  height=160):
        self.heilght = height
        self.name = name
        self.surname = surname
        self.age = age
        Student.student_amount += 1
        self.ns = NameSurname(name, surname)
        self.age = age
        self.height = height
        Student.student_amount += 1
def printStudent(self):
    print(f'Heilght: {self.height}')
    print(f'Name: {self.name}')
    print(f'Surname: {self.surname}')
    print(f'Age: {self.age}')

def Birthday(self):
    self.age += 1
    print(f'Happy Birthday to {self.ns.name}. Now you {self.age}!')

Andriy = Student( "Andriy", "Shal",  13 )

print(f'befor creating Student object {Student.student_amount}')
print(Andriy.heilght, Andriy.name, Andriy.surname, Andriy.age)
print(Student.student_amount)
print(Andriy.student_amount )
print(f'after creating Student object {Student.student_amount}')
