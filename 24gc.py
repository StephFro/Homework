# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
length = len(dna)
numGC = 0

for i in range(length):
	if dna[i] == 'G' or dna[i] == 'C':
		numGC += 1

percentGC = numGC / length
print(f'{percentGC:.2f}')
	


"""
python3 24gc.py
0.42
"""
