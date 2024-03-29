#mcb185.py

#reads files

import sys
import gzip


def read_fasta(filename):
	if filename == '-':
		fp = sys.stdin
	if filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)
	
		
	name = None
	seqs = []
	
	while True:
		line = fp.readline()
		if line == '': break
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				yield(name, ''.join(seqs))
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
			
	yield(name, ''.join(seqs))
	fp.close()
		
gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}
		
def translate(seq, frame = 0):
	seq = seq.upper()
	protein = ''
	frame %= 3
	
	for i in range(frame, len(seq), 3):
		if seq[i:i + 3] not in gcode:
			protein += 'X'
		else:
			protein += gcode[seq[i:i + 3]]
		
	return protein	
	
def reverse(gene):
	revSeq = ''
	gene = gene.upper()
	for i in range(len(gene) -1, -1, -1):
		if gene[i] == 'A': revSeq += 'T'
		elif gene[i] == 'T': revSeq += 'A'
		elif gene[i] == 'G': revSeq += 'C'
		elif gene[i] == 'C': revSeq += 'G'
		else: revSeq += 'X'
	return revSeq
		
		
		
