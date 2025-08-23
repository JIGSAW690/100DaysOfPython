
Day10 introduces us with Functions with Output (return statement)

## Challenge-1 
*****************

We've seen functions with only an execution body, functions with inputs that allow for variation in execution of the function body and now we'll see the final form of functions. Functions that can have outputs.

PAUSE 1
Create a function called format_name() that takes two inputs: f_name and `l_name'.

PAUSE 2
Use the title() function to modify the f_name and l_name parameters into Title Case.

Syntax
You can create a function with a body, input and output like this:

def function_name(input_parameter):
    <body of function that uses input_argument>
    return output
Print vs. Output
Return vs. Display: The return statement is used to give back a value from a function, which can be used later, while print is used to display a value to the console only for the programmer to see.

Solution Reference: Func_With_Output.py

## Challene-2
******************

Functions terminate at the return keyword. If you write code below the return statement that code will not be executed.

However, you can have multiple return statements in one function. So how does that work?

Conditional Returns
When we have control flow, as in the code will behave differently (go down different execution paths) depending on certain conditional checks, we can end up with multiple endings (returns).

e.g.

def canBuyAlcohol(age):
    if age >= 18:
        return True
    else:
        return False
Empty Returns
You can also write return without anything afterwards, and this just tells the function to exit.

e.g.

def canBuyAlcohol(age):
    # If the data type of the age input is not a int, then exit.
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False

Solution Reference: Multi_Return_values.py

## Challenge-3
*******************

You can use docstrings to write multiline comments that document your code.

Syntax
Just enclose your text inside a pair of three double quotes.

e.g.

""" 
My 
Multiline 
Comment 
"""

Documenting Functions
A neat feature of docstrings is you can use it just below the definition of a function and that text will be displayed when you hover over a function call. It's a good way to remind yourself what a self-created function does.

e.g.

def my_function(num):
    """Multiplies a number by itself."""
    return num * num

Solution Reference: Docstrings.py

## Challenge-4
*********************

Calculator Application
--------------------------

The goal is to build a calculator program.

Demo
https://appbrewery.github.io/python-day10-demo/

Storing Functions as a Variable Value
You can store a reference to a function as a value to a variable. e.g.

def add(n1, n2):
    return n1 + n2
    
    
my_favourite_calculation = add
my_favourite_calculation(3, 5)  # Will return 8
In the starting file, you'll see a dictionary that references each of the mathematical calculations that can be performed by our calculator. Try it out and see if you can get it to perform addition, subtraction, multiplication and division.

PAUSE 1
TODO: Write out the other 3 functions - subtract, multiply and divide.

PAUSE 2
TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

PAUSE 3
TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

Functionality
Program asks the user to type the first number.
Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
Program asks the user to type the second number.
Program works out the result based on the chosen mathematical operator.
Program asks if the user wants to continue working with the previous result.
If yes, program loops to use the previous result as the first number and then repeats the calculation process.
If no, program asks the user for the fist number again and wipes all memory of previous calculations.
Add the logo from art.py
 Hint 1 
Try writing out a flowchart to plan your program.
 Hint 2 
To call multiplication from the operations dictionary, you would write your code like this:
result = operations["*"](n1= 5, n2= 3)

result would then be equal to 15.

Solution Reference: Calculator.py