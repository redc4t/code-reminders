name = "John"
print("Hello, %s!" % name) #%s and %d are argument specifiers where %s indicates the insertion of the name from the variable above where the % symbol is

age = 23
print("%s is %d years old." % (name,age)) #insertion of multiple lists into the printed statement

mylist = [1,2,3]
print("A list: %s" % mylist) # prints a list where the argument is specified

# %s - String or any object in string representation
# %d - integers
# %f - Floating point numbers
# %.<number of digits> - floating point numbers with a fixed amount of decimal places
# %x/%X - Integers in hex representation (lowercase/uppercase)