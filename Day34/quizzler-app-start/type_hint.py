
#We can assign a type to a variable using the ':' syntax as given below
a: int
b: float
c: str
d: bool

#We can assign a return type for a function or a method using the '->' syntax as given below
def greeting(s: str) -> str:
    return s

print(greeting("Hello"))