class Student():
    name = 'shaam'
    age = 20
print(Student)
print(getattr(Student,'name'))
print(getattr(Student,'age','Oopies no age'))
print(Student.age)
setattr(Student,'sex','male')
Student.school = 'AVM'
print(Student.school)
print(Student.__dict__)
delattr(Student,'age')
del Student.sex