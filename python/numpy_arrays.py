#create 2 new lists height and weight

height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

#import the numpy array package as np

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height)) # print out the array height

#calculate bmi with arrays

bmi = np_weight / np_height ** 2


### subsetting
## uncomment the below lines for variable response
#bmi > 24 #for boolean response

#bmi[bmi > 24] # print only the observations over 23

print(bmi)