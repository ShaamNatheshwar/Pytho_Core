try:
    file = open('sample.txt','r')
    print(file.readline(2))
    print(file.readlines())
except Exception as e:
    print(e)
    