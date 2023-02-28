# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

#import the library
import sys
import math
import mcb185

#create a function with three arguements
def entropy(filename, x, thres):

	#use the mcb185 library to read the file
	for line, sequence in mcb185.read_fasta(filename):
		seq = ''
		
		for position in range(len(seq - x + 1)):
			seq2 = sequence[position: position + w]
			
			#intialize the needed bases
			A = 0
			T = 0
			G = 0
			C = 0
			
			#increment the bases
			for nucleo in seq2:
				if nucleo == 'A': A += 1
				if nucleo == 'T': T += 1
				if nucleo == 'G': G += 1
				if nucleo == 'C': C += 1
			
			#calculate the probabilities
			probs = [A/x, T/x, G/x, C/x]
			
			#now calculate entropy as we did before
			H = 0
			
			for probal in probs:
				if probs != 0:
					H += -(probs * math.log2(probs))
					
				if H < thres:
					seq3 += 'N'
				else:
					seq3 += seq2[0]
			return line, seq3

#get the variables from the command line
filename = sys.argv[1]
x = int(sys.argv[2])
thres = float(sys.argv[3])

#run the function
line, seq2 = entropy(filename, x, thres)

print(line)

for position in range(0, len(seq3), 60):
	print(seq3[position:position + 60])
					
		


"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
