def my_function():
    print("hello function!")

def my_function_with_args(username, greeting):
    print("Hello! %s, from my function!, I wish you %s" %(username, greeting))

def sum_two_numbers(a,b):
    return a+b

my_function() #call the function

my_function_with_args("John Doe", "a great year!") #call the function while setting the arguments

x = sum_two_numbers(1, 2) #call the function while setting the args in the sum

print(x)


