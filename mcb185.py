#mcb185.py

#reads files

import sys
import gzip


def read_fasta(filename):
	if filename == '-':
		fp.stdin
	if filename.endswith('.gz'):
		fp = gzip(filename, 'rt')
	else:
		fp = open(filename)
		
	name = []
	seqs = []
	
	while True:
		line = fp.readline()
		if line == ' ': break
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				yield(name, ''.join(seqs))
				name = line[1:]
				seq = []
			else:
				seqs.append(line)
		yield(name, '',join(seqs))
		fp.close()
		
		
		
		
		
