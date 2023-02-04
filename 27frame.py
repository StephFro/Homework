# 27frame.py

# Write a program that prints out the position, frame, and letter of the DNA

# Variation: try coding this with a single loop and nested loops

# Note: use 0-based indexing for position and frame (biology uses 1-based)

dna = 'ATGGCCTTT'
frameCount = 0

for i in range(len(dna)):
	info = ''
	info += str(i) + ' '
	
	if frameCount > 2:
		frameCount = 0
		info += str(frameCount) + ' '
		frameCount = int(frameCount)
		frameCount += 1
	else:
		info += str(frameCount) + ' '
		frameCount = int(frameCount)
		frameCount += 1
		
	info += dna[i]
	
	print(info)
	
	


"""
python3 27frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
