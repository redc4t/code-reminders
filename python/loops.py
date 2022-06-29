primes = [2, 3, 5, 7]

for prime in primes: #for every prime number in the 'primes' array
    print(prime) # print the prime numbers

for y in range(5):
    print(y) # prints all of the numbers up to 5

count = 0 #initialise the count
while count < 5: #while the count is less than 5
    print(count) #do this
    count+= 1 #count plus 1

count2 = 0
while True: #while the below statements are true
    print(count2) #print the count2
    count2 += 1 #count + 1
    if count2 >= 5: #if the count is greater than or equal to 5
        break #end the program
for x in range(10): #for x in the range of 0 - 10
    if x % 2 == 0: #check to see if x is even
        continue #skip the current block and return to the for statement
    print(x) #print out x

count3 = 0
while(count3 < 5):
    print(count3)
    count3 +=1
else:
    print("Count Value Reached %d" %(count3))

for i in range(1,10):
    if (i%5==0):
        break
    print(i)
else:
    print("not printed due to the for loop being terminated because of break clause")