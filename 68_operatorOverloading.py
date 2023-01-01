class Addition:
    def __init__(self,a):
        self.a = a
    def __add__(o1,o2):
        return o1.a+o2.a
o1 = Addition(10)
o2 = Addition(20)

print(o1+o2)
        