days = int(input('Enter the delayed days'))
if days == 0:
    print('Good')
elif days >=1 and days <= 5:
    print('Your fine amount is: ', days * 0.5)
elif days >= 6 and days<=10:
    print('Your fine amount is: ', days * 1.5)
else:
    print('Membership cancelled')