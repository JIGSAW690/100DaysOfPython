Today we are introduced to namespaces and scopes in python through a series of challenges and finally we'll be making one fully interactive Number Guessing game where user will be allowed to guess the number 5 or 10 times depending on the difficulty they selects.

## Challenge-1
******************

Local Scope
Variables (or functions) declared inside functions have local scope (also called function scope). They are only seen by other code within the same block of code.

e.g.

def my_function():
    my_local_var = 2
    
# This will cause a NameErrorr
print(my_local_var) 
Global Scope
Variables or functions declared at the top level (unindented) of a code file have global scope. It is accessible anywhere in the code file.

e.g.

my_global_var = 3

def my_function():
    # This works no problems
    print(my_global_var)

Solution Reference: Scope.py

## Challenge-2
**********************

Python is a bit different from other programming languages in that it does not have block scope.

This means that variables created nested in other blocks of code e.g. for loops, if statements, while loops etc. don't get local scope. They are given function scope if they are within a function or global scope if they are not.

e.g.

# Accessible anywhere
my_global_var = 1

def my_function():
    # Only accessible within my_function()
    my_local_var = 2
    
for _ in range(10):
    # Accessible anywhere
    my_block_var = 3


Solution Reference: Block_Scope.py

## Challenge-3
********************

You can force the code allow you to modify something with global if you use the global keyword before you use it.

e.g. This will give you an error

a = 1
def my_function():
    a += 1
    print(a)
But this will work

a = 1
def my_function():
    global a
    a += 1
    print(a)

Solution Reference: Global.py

## Challenge-4
*****************

You can define global constants in your code file for easy access. Their job is meant to be "set and forget" so you can use their values but never need to mofy them.

Naming Convention
Global constants are normally declared in ALL_CAPS with a underscore in between.

e.g.

PI = 3.14159
GOOGLE_URL = "https://www.google.com"

Solution Reference: Constant.py

## Challenge-5
*********************

NUMBER GUESSING GAME

The goal is to build a guess the number game.

Demo
https://appbrewery.github.io/python-day12-demo/

ASCII Art
You can get hold of ASCII art using the link below: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Som

Solution Reference: Number_game.py (My Version)
Solution Reference: Constant.py (Angela's Course Version)