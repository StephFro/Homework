# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers
import random

dna = ''
numAT = 0
numGC = 0

for i in range(30):
	ran = random.randint(1,4)
	if len(dna) > 0:
		if dna[i-1] == 'A' or dna[i-1] == 'T':
			numAT += 1
		else:
			numGC += 1
			ran = random.randint(3,4) 
			#note: after several reps, this results in .57, .6, .63 .66, and .7. Averaging these is about 60%.
	if ran == 1:
		dna += 'G'
	if ran == 2:
		dna += 'C'
	if ran == 3:
		dna += 'A'
	if ran == 4:
		dna += 'T'

print(len(dna))
print(numAT/len(dna))
print(dna)
		
"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
