# 61kmers.py

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

# Hint: use argparse
# Hint: use mcb185.read_fasta()

import argparse
import mcb185


#argparse initalize
parse = argparse.ArgumentParser(description = 'kmers in a fasta file')

parse.add_argument('file', type = str, metavar = '<path>', help = 'fasta file')
parse.add_argument('Klen', type = int, metavar = '<path>', help = 'Size k')

arg = parse.parse_args()

#intialize a dictionary for values
kmers = {}

#Read the file!
for line in mcb185.read_fasta(arg.file):
	#skip headers
	for seq in line[1:]:
		for pos in range(len(seq) - arg.Klen + 1):
			kmer = seq[pos:pos + arg.Klen]
			
			if kmer not in kmers:
				kmers[kmer] = 1
			else:
				kmers[kmer] += 1
				
for kmer in sorted(kmers):
	print(kmer, kmers[kmer])



#error in reading a 'closed file' to be fixed!






"""
python3 60kmers.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 2
AA 338006
AC 256773
AG 238013
AT 309950
CA 325327
CC 271821
CG 346793
CT 236149
GA 267384
GC 384102
GG 270252
GT 255699
TA 212024
TC 267395
TG 322379
TT 339584
"""
