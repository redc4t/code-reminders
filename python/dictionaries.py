#similar to arrays, but works with keys and values instead of indexes

#example phone database
phonebook = {} #initialise dictionary
phonebook['John'] = 93657884 #add key and value jack with corresponding number
phonebook['Jack'] = 77684993
phonebook['Jill'] = 45663445

print(phonebook) #print out the key value pairs

## alternate initilisation of above

phonebook2 = {
    "John" : 47774637,
    "Jack" : 46635373,
    "Jill" : 46839827
}

print(phonebook2)

####iterating over dictionaries

phonebook3 = { "John" : 23332342, "Jack" : 23454323, "Jill" : 23334534
}

for name, number in phonebook3.items():
    print("Phone number of %s is %d" % (name, number))


#####removing values from dictionaries

phonebook4 = {
    "John" : 47774637,
    "Jack" : 46635373,
    "Jill" : 46839827
}

del phonebook4["John"]
print(phonebook4)

##### alternate removal of value

phonebook5 = {
    "John" : 47774637,
    "Jack" : 46635373,
    "Jill" : 46839827
}

phonebook5.pop("John")
print(phonebook5)

