#!/usr/bin/env python 
import re
import sys
infile = sys.argv[1]
outfile =  sys.argv[2]

fasta_dict = {}

with open(infile,'r') as f:
    for line in f:
        ## remove trailing newline (can use line.strip("\n") as well)
        line = line.rstrip()
        ##It's the header 
        if line.startswith('>'):
            ## returns 'gene=XXXX'
            gene_name = line 
        ## It's the nucleotide sequence
        else:
            ## we have seen this header before 
            if gene_name in fasta_dict:
                fasta_dict[gene_name].append(line)
            ## we have seen it before
            else:
                 fasta_dict[gene_name] = []
                 fasta_dict[gene_name].append(line)

with open(outfile, 'w') as f:
    for key in fasta_dict:
        f.write("{}\n".format(key))
        f.write("{}\n".format("".join(fasta_dict[key])))
