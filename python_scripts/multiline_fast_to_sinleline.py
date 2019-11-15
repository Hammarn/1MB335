#!/usr/bin/env python

import sys


input_list = []

fasta_file = sys.argv[1]
counter = 0
with open(fasta_file, 'r') as f:
    for line in f:
        while line.startswith('>'):
            input_list.append(line)
            counter += 1
        else:
            ## append to a list and then add that list to the outer list
            ##
