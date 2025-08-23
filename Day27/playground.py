
# Working with *args
def add(*args):
    print(sum(args))

add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#Working with **kwargs
def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

    n += kwargs['add']
    n *= kwargs['mul']
    print(f'{n}')

calculate(3, add=3, mul=4)
