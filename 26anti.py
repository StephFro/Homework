# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
reverse = ''
revComp = ''

for i in dna:
	reverse = i + reverse #reverse the string

for i in range(len(reverse)): #complement of the reverse
	if reverse[i] == 'A':
		revComp += 'T'
	elif reverse[i] == 'T':
		revComp += 'A'
	elif reverse[i] == 'C':
		revComp += 'G'
	elif reverse[i] == 'G':
		revComp += 'C'
		

print(revComp)
	



"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
