class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetail(self):
        print('Hi I am ', self.name, 'i am ', self.age)
    
    @staticmethod
    def total():
        print('You are  welcome')

o = Person(21, 'govind')
print(o.total())