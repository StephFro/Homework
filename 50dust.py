# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. has option and default value for window size
# 2. has option and default value for entropy threshold
# 3. has a switch for N-based or lowercase (soft) masking
# 4. works with uppercase or lowercase input files
# 5. works as an executable
# 6. outputs a FASTA file wrapped at 60 characters

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

#import what we need
import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description = 'Calculates Entropy')
parser.add_argument('file', type = str, metavar = '<path>', help = 'file')
parser.add_argument('-w', required = False, type = int, default = 11, metavar = '<int>', help = 'int value')
parser.add_argument('-t', required = False, type = float, default = 1.4, metavar = '<float>', help = 'float value')
parser.add_argument('-s', required = False, action = 'store_true', help = 'lower masking')

arg = parser.parse_args()

def entropy(window):
	nucleotides = ['A', 'T', 'C', 'G']
	nucleoCount = [0] * 4
	nuceloProb = []
	
	H = 0
	
	for nucleotide in window:
		if nucleotide in nucleotides:
			nucleoCount[nucelotides.index(nucleotide)] += 1
	
	for count in nucleoCount:
		nucleoProb.append(count/len(window))
		
	for prob in nucleoProb:
		if prob != 0:
			H -= prob * math.log2(prob)
			
	return H
	
def shift(seq, length):
	
	window = seq[:length].upper()
	
	fSeq = seq.upper()
	
	for pos in range(len(seq)):
		if pos in range(len(seq)-length + 1):
			if pos != 0:
				window = window[1:] + seq[pos+length-1]
				
			H = entropy(window)
			
			if H < arg.t and arg.s == True:
				fSeq = fSeq.replace(
					fSeq[pos:pos+length], fSeq[pos:pos+length].lower())
					
			elif H < arg.t and arg.s == False:
				fSeq = fSeq.replace(
					fSeq[pos:pos+length], 'N'*length)
					
		if (pos+1) % 60 == 0:
			yield(fSeq[pos-59:pos+1])
			
		if len(seq) % 60 != 0:
			yield(fSeq[len(seq)-(len(seq)%60):])
			
			
for line in mcb185.read_fasta(arg.file):
	print('>'+line[0])
	for seq in line[1:]:
		for line in shift(seq, arg.w): print(line)


"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGcttttcattctGACTGCAACGGGCAATATGTCTCTGTGTggattaaaaaaagagtgTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGagtaaattaaaattttattgaCTTAGG
TCACtaaatactttaaCCAATATAGGCATAGCGCACAGacagataaaaattacaGAGTac
acaacatccaTGAAACGCATTAGCACCACCATtaccaccaccatcaccaTTACCACAGGT
AACggtgcgggctgACGCGTACAGgaaacacagaaaaaagccCGCACCTGACAGTGCggg
ctttttttttcgaCCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AggcaggggcaggtggCCAccgtcctctctgcccccgccaaaatcaccaaccacctGGTG
GCGATgattgaaaaaaccattaGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
"""
