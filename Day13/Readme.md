In day 13 of 100 days of Python coding, we are introduced to various tips and tricks to debug Python Codes and writing cleaner code for readability through a series of challenges and steps.


## Challenge-1
***************

Steps:: DESCRIBE THE PROBLEM
The first step of solving a problem is being able to describe the problem.

PAUSE 1
Look at the code in task_1.py and answer the following questions:

What is the for loop doing?
When is the function meant to print "You got it"?
What are your assumptions about the value of i?
PAUSE 2
Fix the code so that the print statement executes.

Solution Reference: task_1.py

## Challenge-2
******************

Steps:: REPRODUCE THE BUG.
Some bugs are sneaky, they only occur under certain conditions. In order to debug them, we need to be able to reliably reproduce the bug and diagnose our problem to figure out which conditions trigger the bug.

PAUSE 1
Change the code so that it always produces the occasional error.

PAUSE 2
Fix the code and remove the bug.

Solution Reference: task_2.py

## Challenge-3
*******************

Steps:: PLAY COMPUTER

Playing computer is an important skill in debugging. You need to be able to go through your code line by line as if you were the computer to help you figure out what is going wrong.

PAUSE 1
Play computer and go through the code line by line as if you were executing the code to figure out why 1994 does not work as expected. Then go ahead and fix the code.

Solution Reference: task_3.py

## Challenge-4
*******************

Steps:: FIX THE ERRORS

Fix any errors (red underlines) that show up in the editor before you run your code. The warnings (yellow) are optional fixes, sometimes it will cause a problem down the line other times it's fine and the editor just doesn't understand what you are trying to do.

Solution reference: task_4.py

## Challenge-5
*******************

Steps:: USE PRINT() STATEMENTS

print() is your friend. It can help expose hidden values while your code is running. In a for loop, the loop will follow some rules to perform a repeated block of code. But during the loop it's difficult to see the intermediate values, that's a perfect example of how you can use print to expose those intermediate values and help you debug your code.

PAUSE 1
The code is supposed to calculate the total number of words given the number pages and the word per page. But it's not currently giving any output. Diagnose the problem using print() statements.

PAUSE 2
Fix the code.

Solution Reference: task_5.py

## Challenge-6
*********************

Steps:: USE A DEBUGGER (OF IDE)

Most IDEs (Intelligent Development Environments) such as PyCharm will have built-in tools for debugging. This is normally known as the debugger. In many ways, they are like print statements on steroids.

Debuggers allows us to peek into our code during execution and pause on chosen lines to figure out what is the inner mechanism and where it's going wrong.

There are a couple of things that are the same in most IDEs which you should be familiar with:

Breakpoint - You can set a breakpoint by clicking on a line in the gutter of the code (where the line numbers are). This line will be where the program pauses during debug run.

Step Over - This button will go through the execution of your code line by line and allow you to view the intermediate values of your variables.

Step Into - This will enter into any other modules that your code references. e.g. If you use a function from the random module it will show you the original code for that function so you can better understand its functionality and how it relates to your problems.

Step Into My Code - This does the same thing as Step Into, but it limits the scope to your own project code and ignores library code such as random.

PAUSE 1
Use the PyCharm debugger to figure out what is the issue in the starting code and fix it.

Solution Reference: Debugger.py