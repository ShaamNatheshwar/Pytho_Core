para = []
print('Enter a paragraph')

while True:
    line = input()
    if line:
        para.append(line)
    else:
        break
print(para)
output = '\n'.join(para)
print(output)