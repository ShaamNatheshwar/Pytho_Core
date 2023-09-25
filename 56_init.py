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


see why are we using it is....no matter how many function we call upon name...we can call it from init...so generall stuffs which will be used again and again and needs
a new instance can be done via init


most important
In previous example I will make change inside the mention as if its one class but different function

while using  init
it feels like different class itself

its like 10a 10b new new instance.....whereas using old method we are jst creating a blueprint and make others use it
