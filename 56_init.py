class Person:
    def __init__(self, name):
        print('Instance has been created')
        self.name = name
    def printAll(self):
        print('My name is: ', self.name)

o1 = Person("shaam")
o1.printAll()

o2 = Person("Genichiro")
o2.printAll()
        