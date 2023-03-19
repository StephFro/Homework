# 70gff.py

# Write a program that converts genes in gff into JSON
# Use the E. coli genome gff
# Your code should mimic the output below

import json
import argparse
import gzip
import re

parser = argparse.ArgumentParser(description='GFF -> json')
parser.add_argument('file',type=str, metavar= '<path>', help='GFF')
arg = parser.parse_args()

genome = []

with gzip.open(arg.file, 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		for matches in re.finditer('RefSeq\sgene', line):
			all = {}
			
			#do the search
			coordinate = re.search('(\d+)\s(\d+)', line)
			begin = int(coordinate.group(1))
			ending = int(coordinate.group(2))
			
			st = re.search('\.\s(.)\s\.', line)
			strand = st.group(1)
			
			name = re.search('Name=(\w+)', line)
			gene = str(name.group(1))
			
			#dictionary
			all['gene'] = gene
			all['begin'] = begin
			all['ending'] = ending
			all['strand'] = strand
			
			genome.append(all)
			
print(json.dumps(genome, indent=4))





"""
python3 70gff.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gff.gz
[
    {
        "gene": "thrL",
        "beg": 190,
        "end": 255,
        "strand": "+"
    },
    {
        "gene": "thrA",
        "beg": 337,
        "end": 2799,
        "strand": "+"
    },
...
"""
