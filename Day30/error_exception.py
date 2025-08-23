#FileNotFoundError
try:
    with open('a.txt', 'w+') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print('File not found')
else:
    print('File found')
finally:
    print('This line will be always printed')

#TypeError
b = 5
print(b + 'string')

#KeyError
a = {'a': 1, 'b': 2, 'c': 3}
print(a['d'])

