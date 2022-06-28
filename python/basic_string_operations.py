astring1 = "Hello World"
# strings can be defined with either single or double quotation marks

print("single quotes are ' '") #when using apostraphes or quotes within a string, use double quotation marks to prevent single quotation marks breaking the string
print(len(astring1)) # len function counts the length of the string and returns the integer

print(astring1.index("o")) #prints the index of the letter specified in quotation marks

print(astring1.count("l")) #.count counts the number of occurences of the specified letter within the string

print(astring1[3:7]) #prints a slice of the string from the 3rd index to the 7th index

print(astring1[3:7])
print(astring1[3:7:1]) # extended slice index in format [start:stop:step]

print(astring1[::-1]) # reverses the string using the index

print(astring1.upper()) #creates a new string by making all of the old string upper case

print(astring1.lower()) # same as above except transforms it to lower case

print(astring1.startswith("Hello")) #creates a string that uses the initial variable but adds 'hello' to the beginning
print(astring1.endswith("asdfasdf")) #creates a string that uses the initial variable but adds 'asdfasdf' onto the end

affewwords = astring1.split(" ") #splits the string into a bunch of strings in a list which are split by the ' ' space

print(affewwords)