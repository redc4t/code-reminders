import random
x = (random.randint(0,10)) #assign x as random integer between 0 and 10

if x == (x % 2) == 0:       #if random x is even, print goodbye
    print ("Goodbye!")
else:
    print("Hello World!")   #if x isn't even, print hello world
