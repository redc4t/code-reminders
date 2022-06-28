x = 2
print(x == 2) #boolean check true or false, x is equal to 2
print(x == 3) #bool check if x == 3
print(x < 3) #bool check if x is less than 3

name = "John"
age = 23
if name == "john" and age == 23: #boolean check to see if name is john and age is 23
    print("Your name is" + "" + name + " your age is " + age) #if check is successful print out result 

if name == "John" or name == "Rick":
    print("your name is either John or Rick.") #boolean check to see if name is either equal to john or Rick

if name in ["John", "Rick"]:
    print("1") #checks to see if the name is within a list

statement = False
another_statement = True
if statement is True:
    #do an action
    pass
elif another_statement is True: #else if
    #do something else
        pass
else:
    #do another thing
        pass

x1 = [1,2,3]
y1 = [1,2,3]

print(x1 == y1) #checks to see if the data within the variables is equal
print(x1 is y1) #checks to see if x1 is y1

print(not False) # prints out true
print((not False) == (False)) #prints out false