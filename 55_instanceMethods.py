class Person:
    name = 'Shaam'
    age = 20
    def myFunc(self, gender):
        print('My name is: ', Person.name)
        print('My name is: ', Person.age)
        print('My gender is: ', gender)

o = Person()
o.myFunc('Male')
# Person.myFunc(o)

