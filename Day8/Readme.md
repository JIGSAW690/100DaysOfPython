## Challenge-1
******************

Functions with Input
---------------------

Previously, we've seen that functions allow us to package code into a named block which can be used repeatedly at a later point.

PAUSE 1 - Review
Create a function called greet().
Write 3 print statements inside the function.
Call the greet() function and run your code.
Inputs
By adding a variable name inside the parentheses when we create (define) a new function, it allows that function to take inputs when called.

That means we can modify how the function behaves each time by passing in different inputs.

# Creating the function
def myFunction(input):
    print(f"Hey! {input}")
# Using the function
myFunction("Tommy") 
# Will output "Hey! Tommy"
Inputs are Variables
When you create a function with inputs, you are defining a variable name that will be given to the data that is passed in.

The name of the input variable, e.g. name in this code here: def greet(name): is called the parameter.

The value of the value of the input variable, e.g. Angela when you call the previous greet function: greet("Angela") is called the argument.

Solution Reference: Greet.py

## Challenge-2
*******************
Multiple Inputs
You can have multiple inputs in functions. All you need to do is separate them with a comma ,.

PAUSE 1
Create a function with multiple inputs

 Hint 1 
def greet(name, greeting):
____print(f"{greeting} {name}")
greet("Angela", "Yo!")

PAUSE 2
Modify the function so that it prints the expected values.

def greet_with(name, location)
    Hello name
    What is it like in location
Positional Arguments
By default, when you create a function in Python, it will keep the order of arguments in the function definition.

e.g. In the function below, the first argument that goes in will always be printed before the second one. a = 2, b = 1

def my_function(a, b)
  print(a)
  print(b)
  
 my_function(2, 1)
 #It will print:
 # 2
 # 1
Keyword Arguments
You can use keywords when you provide the arguments when you call a function so that there is less confusion which value is assigned to which input parameter.

PAUSE 3
Call the greet_with() function using keyword arguments.

 Hint 2 
greet_with(location="London", name="Angela")

Solution Reference: Greet_with_multiple_inputs.py

## Challenge-3
******************

Caesar Cipher
----------------
You are going to build an encryption and decryption program using the Caesar cipher.

Demo
https://appbrewery.github.io/python-day8-demo/

TODO-1:
Create a function called encrypt() that takes original_text and shift_amount as 2 inputs.

TODO-2:
Inside the 'encrypt' function, shift each letter of the original_text forwards in the alphabet by the shift_amount and print the encrypted text.

You can use the built-in Python index() function to find out the position of an item in a list. e.g.

fruits = ["Apple", "Pear", "Orange"]
fruits.index("Pear") #1
e.g. If we have following values:

plain_text = "hello"
shift_amount = 1
The final encrypted output should be:

Here is the encoded result: ifmmp

Where each of the letters of 'hello' is shifted up by 1.

 Hint 1 
Let's breakdown the problem:
You need a for loop to loop through each of the letters in the plain_text.
Find the position of each letter in the alphabet List
Add the user desired shift_amount to the position to get the position of the encoded letter.
Find the corresponding letter for that position.
Add each encoded letter to a new string and print it out after the loop ends.
TODO-3:
Call the encrypt() function and pass in the user inputs. You should be able to test the code and encrypt a message.

TODO-4:
What happens if you try to shift the letter 'z' forwards by 9? Can you fix the code?

 Hint 2 
There are many approaches to do this. 1. You can add more than 1 set of the alphabet into the List of alphabet letters. 2. You can shift the shift_amount so that it is always within 0 - 25 and fits in the List. 3. You can use the modulo to get the remainder.

Solution Reference: CaesarCipher-1.py

## Challenge-4
******************

TODO-1:
Create a function called decrypt() that takes original_text and shift_amount as 2 inputs.

TODO-2:
Inside the decrypt() function, shift each letter of the original_text forwards in the alphabet backwards by the shift_amount and print the decrypted text.

 Hint 1 
TODO-3:
Combine the encrypt() and decrypt() functions into a single function called caesar().
Use the value of the user chosen direction variable to determine which functionality to use.
call the caesar function instead of encrypt/decrypt and pass in all three variables direction/text/shift.
 Hint 2 
Remember that when you multiply a number by -1 it will reverse its sign. e.g. 3 + ( 5 * -1) is the same as 3 - 5.
 Hint 3 
It should say:
Here is the encoded result: XXX

or

Here is the decoded result: XXX

Solution Reference: CaesarCipher-2.py

## Challenge-5
***********************

TODO-1:
Import and print the logo from art.py when the program starts.

TODO-2:
What happens if the user enters a number/symbol/space that's not in the List alphabet?

Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?

e.g.

original_text = "meet me at 3!"
cipher_text = "XXXX XX XX 3!"
 Hint 1 
If it's not a letter in the List alphabet, maybe you can just add it to the end of cipher_text as the unmodified character?
TODO-3:
Can you figure out a way to restart the cipher program?

e.g.

Type 'yes' if you want to go again. Otherwise, type 'no'.

If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again.

 Hint 2 
Try creating a while loop that continues to execute the program if the user types 'yes'.

Solution Reference: CaesarCipherFinal.py