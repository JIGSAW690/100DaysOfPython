## Challenge-1
************************
Condition Check
Learn to use conditionals in Python to check a conditions and tell the computer what to do in each case. e.g.

if <this condition is true>:

    <then execute this line of code>

What if the condition is false?
The else keyword is used to define a block of code that will execute if the condition checked in the if statement is false.

if pigs can fly:

    <Some code that will never execute>

else:

    print("This is real life")

Python Indentation
Understand the importance of indentation in Python as a way to make certain lines of code subsidaries of other lines of code.

e.g.

if 5 > 2: #This is a parent line of code

    print("yes") #this is a child line of code

Comparator Operators
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to
== Equal to
!= Not equal to

Solution reference: RollerCoaster.py

## Challenge-2
************************
The modulo operator gives you the remainder of a division.

6 % 2 #will be 0

6 % 5 #will be 1

6 % 4 #will be 2

PAUSE 1 - What is 10 % 3?
What do you think this will output?

print(10 % 3)

PAUSE 2 - Check Odd or Even
Write some code using what you have learnt about the modulo operator and conditional checks in Python to check if the number in he input area is odd or even. If it's odd print out the word "Odd" otherwise printout "Even".

Solution Reference: Even-Odd.py

## Challenge-3
***************************

Nesting & Elif

You can put if/else statements inside other if/else statements. This is known as nesting. e.g.

if maths_score >= 90:
    if english_score >= 90:
        print("You're good at everything")
    else:
        print("You're good at maths")
if english_score >= 90:
    print("You're good at english)
In this case only when a student has over 90 on maths and english, do they get "You are good at everything".

Note: You can also have if statements that don't have a paired else statement.

Solution Reference: Nested.py

## Challenge-4
*****************************

Multiple Ifs

You can write as many if statements as you need to check for different conditions that are unrelated to each other. Compare the code blocks below:

$$ If/elif/else $$
if <condition 1 is true>
    <do A>
elif <condition 2 is true>
    <do B>
else
    <do C>
$$ Nested if statements $$
if <condition 1 is true>
    <do A>
    if <condition 2 is true>
        <do B>
        if <condition 3 is true>
            <do C>
$$ Multiple if statements $$
if <condition 1 is true>
    <do A>
if <condition 2 is true>
    <do B>
if <condition 3 is true>
    <do C>
In the if/elif/else block, only one of A, B, or C can happen, because if/elif/else are mutually exclusive. The first condition has to fail to go into the elif and the elif (or multiple elif) have to fail to go into the else. Condition 2 is only checked if condition 1 is false.

In the nested if statements, A, B and C can all happen, but conditions 1, 2 and 3 must all be true. The computer will only check condition 2 if condition 1 is true.

In the multiple if statements, A, B, and C can all happen. But they are completely independent of each other. C can happen even if A and B don't. Every condition is checked, no matter the result of the others.

Solution Reference: Multi-If.py

## Challenge-5
************************************

Pizza Order Program

Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

Example Interaction
Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: L
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N: N
Your final bill is: $28.


Solution Reference: Pizaa-Order.py

## Challenge-6
*******************************

You can combine different conditions using logical operators.

A and B #Both conditions need to be true
C or D #Only one condition needs to be true
not E #The condition must be false

PAUSE 1 - Age 45 to 55 Modifier
Update the code so that people age 45 to 55 (inclusive of both ages) ride for free. Use logical operators to check that the age is greater than 45, and it's also less than 55.

NOTE: The warning for simplification is just a suggestion. You can consider it and chose it, or you can ignore it. In this lesson I wanted to show you the and, or and not logical operators. So I recommend keeping the original code in case you come back to this lesson for review.

Solution Reference: RollerCoasterFinal.py

## Challenge-7
*************************************

Tresure Hunt App

Your goal today is to build a "Chose your own adventure game". Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.

Use the flow chart linked below to create the game logic. 
https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D

Once you've completed the project, you can always extend the game and make it more interesting!

Solution Reference: Tresure-Hunt-Game-App.py
