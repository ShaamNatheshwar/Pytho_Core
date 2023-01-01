a = {'shaam','Ram'}
print(a)
print(type(a))
a.add('Gohan')
b = {'gogeta'}
a.update(b)
a.remove('Ram')
a.discard('Gohan')
a.pop()
print(a)
# a.clear()
# del a

a = {1,2,3}
b = {'a','b','c'}
c = a.union(b)
print(c)

x = {1,2,4,3}
y = {4,5,6}
# d = x.intersection(y)
# x.intersection_update(y)
d = x.symmetric_difference(y)
x.symmetric_difference_update(y)
print(d,x)

j = {1,2,4}
k = {1,2,4}
l = j.issuperset(k)
v = j.issubset(k)
n = j.isdisjoint(k)
print(v,l,n)