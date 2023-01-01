class Person:
    name = 'shaam'
    age = 20
    def myPrint():
        print('My name is: ',Person.name)
        print('My age is: ',Person.age)

getattr(Person,'myPrint')()
Person.__dict__['myPrint']()