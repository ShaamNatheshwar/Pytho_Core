try:
    file = open('sample.txt','r')
    for i in file:
        print(i)
        
except Exception as e:
    print(e)
    