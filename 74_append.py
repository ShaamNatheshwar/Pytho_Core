try:

    file = open('sample.txt',"a")
    file.write('This is beyblade movie boss')
    file.close()
    file = open('sample.txt','r')
    for i in file:
        print(i)
        
except Exception as e:
    print(e)
    