#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
## Usage: python code_skeleton_question2.py inputfile.fasta 

## sys.argv[1] is the second argument given  
input_file = sys.argv[1]

with open(input_file, 'r') as f:
    ## If you want to read it all at once use f.read or f.readlines() 
    ## and save that to a variable
    
    ## Reading the file line by line
    for line in f:
        #line is a string

