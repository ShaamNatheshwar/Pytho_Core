a = [1,2,3,4,5]
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[1:])
print(a[:5])
a[0] = 100
print(a)
b = [1,True, 'Shaam',[2,3,4,5]]
print(type(b[0]))
print(type(b[1]))
print(type(b[2]))
print(type(b[3]))
print(b[3][3])
print(a)
# a.clear()
c = b.copy()
print(c.count(1))
print(c.index(1))
print(len(a))
print(max(a))
print(min(a))
a.pop(3)
print(a)
a.remove(2)
print(a)

names = ['shaam']
names.append('natheshwar')
names.append('ssn')
print(names)

girls = ['a','b','c']
names.extend(girls)

names.insert(0,'Gogeta')
print(names)

print(list('TURtel'))

values = [20,30,320,50]
print(values.sort(reverse=True))
# print(values.sort(key=len))use this only for str