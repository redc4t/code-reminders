class MyClass: #define class
    variable = "blah" #variable assigned to the class

    def function(self): #set a function to be called from within the class
        print("This is a message inside a class")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity" #set the variable of 'myobjecty' to 'yackity'

print(myobjectx.variable) #print the variables assigned to the objects
print(myobjecty.variable)

myobjectx.function()

##############################################

class NumberHolder:

    def __init__(self, number): #initialises the class
        self.number = number
    def returnNumber(self):
        return self.number
var = NumberHolder(7)
print(var.returnNumber()) # print the variable assigned to var

