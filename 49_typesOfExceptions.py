# print(dir(locals()['__builtins__']))
# print(len(dir(locals()['__builtins__'])))

#Name Error

# try:
#     print(a)
# except NameError as n:
#     print(n)

#zero division

# try:
#     a = 10/0
# except ZeroDivisionError as z:
#     print(z)

# valueError
# try:
#     a = int('Shaam')
# except ValueError as v:
#     print(v)

#index error
# try:
#     a = [10,20,40]
#     print(a[101])
# except IndexError as e:
#     print(e)

#file not found
# try:
#     f = open('ssn.txt')
# except FileNotFoundError as f:
#     print(f)
# else:
#     print(f.read())

#multiple file exception

try:
    a = 10/0
    b = open('ssn.txt')
except ZeroDivisionError as z:
    print(z)
except FileNotFoundError as f:
    print(f)

