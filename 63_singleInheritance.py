class Nokia:
    name = 'Nokia'
    company = 'NokiaIndia'
    def address(self):
        print('Address : salem TamilNadu')
class Nokia1130(Nokia):
    def __init__(self) -> None:
        super().__init__()
        self.year = 1998

    def productDetails(self):
        print('Name of the company: ', self.name)
        print('year of Manufacture: ', self.year)

o = Nokia1130()
print(o.productDetails())