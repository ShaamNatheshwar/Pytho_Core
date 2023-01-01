m1 = int(input('Enter the mark'))
m2 = int(input('Enter the mark2'))
m3  = int(input('Enter the mark3'))
total = m1+m2+m3
average = total / 3.0
if m1>=35 and m2>=35 and m3>= 35:
    print('The total is : ', total)
    print('The average is : ', average)
    if average >= 90 and average <=100:
        print('You scored S grade')
    elif average >= 80 and average <= 89:
        print('you the A grade')
else:
    print('Failed')
    print('No grade available')