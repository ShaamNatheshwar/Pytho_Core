class Student:
    def __init__(self, total):
        self._total = total
    def avg(self):
        return self._total / 5
    @property
    def total(self):
        return self._total
    

    @total.setter
    def total(self, t):
         self._total = t

o = Student(470)
print(o.total)
print(o.avg())     