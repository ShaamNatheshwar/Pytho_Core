class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def printDetail(self):
        print('Hi I am ', self.name, 'i am ', self.age)
    
    @classmethod
    def total(cls):
        return Person.count

o = Person(21, 'govind')
print(o.total())
print(Person.total())