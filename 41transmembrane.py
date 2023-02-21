# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane

import sys
import gzip

#intialize for reference
aminoAcids = ['I', 'V', 'L', 'F', 'C', 'M', 'A', 'G', 'T', 'S', 'W', 'Y', 'P', 'H', 'E', 'Q', 'D', 'N', 'K', 'R']

hydropathy = [4.5, 4.2, 3.8, 2.8, 2.5, 1,9, 1.8, -.04, -.07, -.08, -.09, -1.3, -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5] 

#for cases that give incorrect arguements
if len(sys.argv) != 2:
	print("Bad input. Try again")
	sys.exit()

#take the file	
filename = sys.argv[1]

#function that reads the file
def read(filename):
	record = []
	sequence = ''
	with gzip.open(filename, 'rt') as fp:
		for line in fp.readlines():
			line = line.rstrip()
			if len(line) == 0: continue
			if line[0] == '>':
				if sequence != '':
					record.append(id)
					record.append(sequence)
				word = line.split()
				id = word[0][1:]
				sequence = ''
			else:
				sequence += line
		record.append(id)
		record.append(sequence)
	return record		
	

#function that calcuates the KD	
def kdCalculation(seq):
	sum = 0
	for i in range(len(seq)):
		for j in range(20):
			if dna[i] == aminoAcid[j]: sum += hydropathy[j]
	return sum/len(seq)

#see if proline is present or not	
def proline(seq):
	for amino in seq:
		if amino == 'P': return False
	return True

#function that calculates helix
def helix(seq, length, threshold):
	for i in range(len(seq) - length - 1):
		peptide = seq[i:i+length]
		if proline(peptide): continue
		if kdCalculation(peptide) > threshold: return True
	return False

for seq in read(filename):
	if helix(filename[0:30], 8, 2.5) and helix(filename[30:], 11, 2.0):
		print(seq)
					


"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
