a = (1,2,3,True,'shaam')
print(a)
print(type(a))
print(a[1])
print(a[1:5])
print(a[:5])
print(a[1:])
print(a[-1])
b = list(a)
b.append('goku')
a = tuple(b)
print(a)
for i in a:
    print(i)
if 'shaam' in a:
    print('Yeahhh')
else:
    print('Noooo')


a = (10,)
print(type(a))

del a

a = (1,2,4,3)
b = (3,4,5,6,7)
c = a+b

print(c)
print(c.count(4))
d = (2,4,7)
e = (3,9,1)
f = (d,e)
print(f[0][2])

x = ('shaam',)*10
print(x)

y = (1,2,4)
print(min(y))
print(max(y))

