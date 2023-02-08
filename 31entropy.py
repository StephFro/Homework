# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input


#import library for command line inputs and math
import sys
import math

#create list without leading title, intialize variables
list = sys.argv[1:]
tot = 0

for i in range(len(list)):
	#transform each element to a float
	list[i] = float(list[i])
	

for i in range(len(list)):
	#sum the list for a test later
	tot += list[i]
	
#in case of numbers not summing to 1.0
if tot != 1:
	print('Probabilites do not sum to 1.0. Please try again.')
else:
	H = 0
	for i in range(len(list)):
		#the entropy calculation for each element in the list
		H = H + -(list[i] * math.log(list[i],2))
	print(f'{H:.4}')







"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
