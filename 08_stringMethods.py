s = 'shaamnatheshwar'
print(type(s))
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.find('a'))
print(s.replace('a','r'))
print(s.isalnum())
print(s.isalpha())
print(s.count('s'))
print(s.endswith('r'))
a = "I am \n shaam \n I am good"
print(a.splitlines(True))
b = "This is shaam"
print(b.split(" "))
c = "    shaam  "
print(len(c))
print(len(c.rstrip()))
print(len(c.lstrip()))
d = "20-03-2002"
print(d.partition("-",))