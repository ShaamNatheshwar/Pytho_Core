class Dad:
    def fishing(self):
        print('fishing')
    def chess(self):
        print('chess')

class Mom:
    def cook(self):
        print('Cooking')
    def chess(self):
        print('chess')

class Son(Dad,Mom):
    def play(self):
        print('playing')
o = Son()

o.chess()