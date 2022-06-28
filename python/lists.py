newlist=[]
newlist.append(1)
newlist.append(2)
newlist.append(3)
newlist.append(4)
newlist.append(5)

print(newlist[0]) #print 0th index of list
print(newlist[1]) #print 1st index of list

print(newlist[1:3]) #print index 1 - 2 of list with constraints
print(newlist[:]) #print entire list with open indexing
#print entire list
for x in newlist:
    print(x)
