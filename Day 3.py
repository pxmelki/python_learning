'''
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#2myvar = "John"
#my-var = "John"
#my var = "John"
#This example will produce an error in the result

'''
Camel Case
Each word, except the first, starts with a capital letter:
myVariableName = "John"

Pascal Case
Each word starts with a capital letter:
MyVariableName = "John"

Snake Case
Each word is separated by an underscore character:
my_variable_name = "John"
'''