Day-9 introduces us to Python Dictionaries

## Challenge-1
******************

A dictionary in Python functions similarly to a dictionary in real life. It's a data structure that allows us to associate a key to a value and pair the two pieces of data together.

This is how you create a dictionary in Python:

# An example dictionary
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}

This is how you retrieve items from a dictionary:

print(colours["pear"])
#Will print "green"
This is how to create an empty dictionary:

my_empty_dictionary = {}
This is how you can add new items to an existing dictionary:

colours["peach"] = "pink"
This is also how you can edit an existing value in a dictionary:

colours["apple"] = "green"
This is how to loop through a dictionary and print all the keys:

for key in colours:
    print(key)
This is how to loop through a dictionary and print all the values:

for key in colours:
    print(colours[key])

Solution Reference: Dict.py

## Challenge-2
***********************

Nested Lists and Dictionaries::
--------------------------------------
You can mix and match various data types to achieve your desired structure.

Nesting a List inside a Dictionary
Instead of a String value assigned to a key, we can replace it with a List. You can nest a List in a Dictionary like this:

my_dictionary = {
    key1: [List],
    key2: Value,
}
PAUSE 1
See if you can figure out how to print out "Lille" from the nested List called travel_log.

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
 Hint 1 
To get this part: ["Paris", "Lille", "Dijon"] You would need: travel_log["France"]
Therefore to get Lille, you need: travel_log["France"][1]

Nesting Lists inside other Lists
We've previously seen Nested Lists:

nested_list = ["A", "B", ["C", "D"]]
PAUSE 2
Do you remember how to get items that are nested deeply in a list? Try to print "D" from the list nested_list.

 Hint 2 
To get this list: ["C", "D"] we need the code:
nested_list[2]

Therefore, to get "D" we need:

nested_list[2][1]

Nesting a Dictionary inside a Dictionary
You can also nest a dictionary in a dictionary:

my_dictionary = {
    key1: Value,
    key2: {Key: Value, Key: Value},
}
PAUSE 3
Figure out how to print out "Stuttgart" from the following list:

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}

Solution Reference: Nested_dict.py

## Challenge-3
***************

The goal is to build a blind auction program.

Demo
https://appbrewery.github.io/python-day9-demo/

Clearing the Output
There are several ways of clearing the output. The easiest is to simply print "\n" many times so that the output scrolls down many lines.

e.g.

# This will add 20 new lines to the output
print("\n" * 20)
Functionality
Each person writes their name and bid.
The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines) then loops back to asking name and bid.
Each person's name and bid are saved to a dictionary.
Once all participants have placed their bid, the program works out who has the highest bid and prints it.
 Hint 1 
Try writing out a flowchart to plan your program.
 Hint 2 
The values that come from the input() function are Strings, you'll need to use the int() function to convert it to a number.
Flowchart
If you want to see my flowchart, you can download it here.

Solution Reference: Blind-Auction-App.py