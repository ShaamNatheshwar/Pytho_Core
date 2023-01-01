from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def load(self):
        pass

class HDFC(Bank):
    def load(self):
        # return super().load()
        print('we give load')

o = HDFC()
o.load()