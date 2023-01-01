try:

    file = open('sample.txt',"w")
    file.write('This is beyblade movie boss')
    file = open('sample.txt','r')
    for i in file:
        print(i)
        
except Exception as e:
    print(e)
    