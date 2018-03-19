'''
Homework4: Problem 1 - Dictionaries
Inside of a Jupyter notebook create a dictionary with a one sentence definition of all the concepts we covered.

Use a loop to create an output that looks something like this:

Dictionary: A collection of key-value pairs.

String: A series of characters.

Boolean Expression: An expression that evaluates to True or False.

Comment: A note in a program that the Python interpreter ignores.

Value: An item associated with a key in a dictionary.

Loop: Work through a collection of items, one at a time.

List: A collection of items in a particular order.

Key: The first item in a key-value pair in a dictionary.

Float: A numerical value with a decimal component.

'''

definitions = {'Dictionary':'A collection of key-value pairs.',"String":"A series of characters.","Boolean Expression":"An expression that evaluates to True or False.","Comment":"A note in a program that the Python interpreter ignores.","Value":"An item associated with a key in a dictionary.","Loop":"Work through a collection of items, one at a time.","List":"A collection of items in a particular order.","Key":"The first item in a key-value pair in a dictionary.","Float":"A numerical value with a decimal component."}

for defnumber in definitions:
    print('{}: {}'.format(definitions.key(),definitions.val()))
