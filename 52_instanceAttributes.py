class Person:
    course = 'Java'

o = Person()
print(Person.__dict__)
print(o.__dict__)
print(o.course)
o.course = 'MachineLearning'
print(o.__dict__)

o2 = Person()
print(o2.__dict__)
