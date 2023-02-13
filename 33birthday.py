# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

#import sys and random
import sys
import random

#create a list from command line without leading title
list = sys.argv[1:]

#get variables from list
days = int(list[0])
people = int(list[1])

prob = 0


#For a proper probability count, multiple trials must happen
trials = 10000

#go thru the trials
for j in range(trials):
	match = 0
	birthday = []
	#make a list of days with all 0's
	for i in range(days):
		birthday.append(0)
	#go thru all the people and give them a birthday
	for x in range(people):
		bday = random.randint(0, days - 1)
		birthday[bday] = birthday[bday] + 1
	#go thru the birthday list, and if there is two birthdays,
	#call it a match and increase prob
	for number in birthday:
		if number > 1:
			match += 1
		if match > 0:
			prob += 1
			match = 0
			break
	

result = prob / trials
	

print(f'{result:.3}')


"""
python3 33birthday.py 365 23
0.571
"""

