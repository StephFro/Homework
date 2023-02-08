# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

#import the library
import sys 

#create list to work with, excluding title
list = sys.argv[1:] 
count = 0 
sum = 0 


#go thru the length of the list
for i in range(len(list)): 
	#transform each element to an int
	list[i] = int(list[i])
	#increment count, for count of elements in list 
	count += 1 
	#sum of all the elements in the list
	sum += list[i] 

	
#the minimum number in the list
mini = min(list)
 
#the maximum number in the list
maxi = max(list)

#average, sum of the elements / total elements 
ave = sum/count 

sumsub = 0

#again thru the list
for i in range(len(list)):
	#intialize at the beginning of each loop 
	submeansq = 0 
	#subtract the mean from the element at position i, and square it
	submeansq = (ave - list[i]) ** 2 
	#sum of all the above
	sumsub += submeansq 

#average of the deviations for the mean of the standard deviation
stdmean = sumsub / count 

#square root to get the standard deviation!
std = stdmean ** .5 

#sort the list for the median
list.sort()
 
#the middle of the list
middle = (len(list) - 1) // 2 

#if the list is odd in length
if len(list) % 2 == 1: 
	#median is the element in the middle
	median = list[middle] 
else:
	#median is the average of the two middle values
	median = (list[middle] + list[middle + 1]) / 2 
	



print(count)
print(float(mini))
print(float(maxi))
print(f'{ave:.3f}')
print(f'{std:.3f}')
print(f'{median:.3f}')



"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
