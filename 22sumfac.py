# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library

factorial = 1 
sum = 0 #intialized for later
n = 5 #later could be changed to input: so user can choose

for i in range(1, n + 1): #+1 so it goes thru all
	sum += i
	factorial *= i

print(n)
print(sum)
print(factorial)

"""
python3 22sumfac.py
5 15 120
"""
