# 63canonical.py

# You probably learned that ATG is the only start codon, but is it?
# Write a program that reports the start codons from the E. coli genome
# Your program must:
#    1. read GCF_000005845.2_ASM584v2_genomic.gbff.gz at the only input
#    2. use a regex to find CDS coordinates
#    3. count how many different start codons there are

# Note: the sequence is at the end of the file
# Note: genes on the negative strand are marked complement(a..b)

# Hint: you can read a file twice, first to get the DNA, then the CDS
# Hint: check your CDS by examining the source protein

import argparse
import re
import gzip
import mcb185


parser = argparse.ArgumentParser(description = 'Start Counter')
parser.add_argument('file', type = str, metavar = '<path>', help='file')
arg = parser.parse_args()


seq = ''
codons = {}

with gzip.open(arg.file, 'rt') as fp:
	for line in fp:
		if line.startswith('ORIGIN'):
			break
		for line in fp:
			f = line.split()
			seq += ''.join(f[1:])
				
				
seq = seq.upper()

with gzip.open(arg.file, 'rt') as fp:
	for line in fp:
		for match in re.finditer('\s(CDS)\s', line):
			
			coordinate = re.search('(\d+)\.\.(\d+)', line)
			begin = int(coordinate.group(1))
			end = int(coordinate.group(2))
			
			if 'complement' in line:
				codon = mcb185.reverse(seq[end-3: end])
			else:
				codon = seq[begin - 1: begin + 2]
			
			if codon not in codons:
				codons[codon] = 0
			
			codons[codon] += 1
			
for x in codons:
	print(x, codons[x])

#alter so output doesn't have nonsense 

"""
python3 63canonical.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gbff.gz
ATG 3883
GTG 338
TTG 80
ATT 5
AGT 1
AAA 1
AGC 1
TTC 1
TAA 1
CGT 1
CTG 2
GAC 1
"""
