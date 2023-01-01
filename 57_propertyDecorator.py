class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property    
    def Updated(self):
        return'Hi!!! my name is : ' + self.name + 'I am ' + str(self.age) + 'Thank you'

o = Person('shaam', 20)
print(o.Updated)
        