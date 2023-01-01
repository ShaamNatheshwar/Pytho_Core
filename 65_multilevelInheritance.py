class GrandDad:
    def ownHouse(self):
        print('House')

class Dad(GrandDad):
    def ownBike(self):
        print('Bike')
class son(Dad):
    def cycle(self):
        print('Cycle')

o = son()
o.ownHouse()