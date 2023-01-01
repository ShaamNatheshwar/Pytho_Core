try:
    file = open('sample.txt','r')
    print(file.read())

except Exception as e:
    print(e)

else:
    print('Thank you')