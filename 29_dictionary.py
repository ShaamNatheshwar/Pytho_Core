a = {
    'name':'shaam',
    'age':20
}
print(a)
print(type(a))
print(a.get('name'))
print(a.values())
print(a.keys())
print(a.items())

for i in a:
    print(a[i])
for i in a:
    print(a.values())

if 'gender' in a:
    print('yESS')
else:
    print('nope')

a.update({'school':'AVM'})
a.pop('age')
print(a)
a.clear()

user = {
    'user1':{
        'name':'shaam',
        'age': 20
    }
}

print(user['user1']['age'])