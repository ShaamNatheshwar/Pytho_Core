class Student:
    def __init__(self, total):
        self._total = total
    def avg(self):
        return self._total / 5
    
    def getter(self):
        return self._total
    

    
    def setter(self, t):
         self._total = t
    
    total = property(getter,setter)

o = Student(450)
print(o.total)
print(o.avg())     