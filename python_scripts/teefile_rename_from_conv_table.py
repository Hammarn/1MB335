#!/usr/bin/env python
import argparse

col_1 = []
col_2 = []
col_3 = []

def main(args):
    with open(args.treefile, 'r') as tree_file:
        tree_string = tree_file.read()
    with open(args.conversion, 'r') as f:
        for line in f:
            # Skip empty lines
            if line in ['\n', '\r\n']:
                next
            line = line.rstrip() 
            line =  line.split("\t")
            col_1.append(line[0])
            col_2.append(line[1])
            col_3.append(line[2])
            
    
    if args.to_numb == "1":
        col_to_use = col_1
    elif args.to_numb == "2":
        col_to_use = col_2
    elif args.to_numb == "3":
        col_to_use = col_3

    if args.from_numb == "1":
        tree_string = replace_string(col_1, col_to_use, tree_string)
    elif args.from_numb == "2":
        tree_string = replace_string(col_2, col_to_use, tree_string)
    elif args.from_numb == "3":
        tree_string = replace_string(col3, col_to_use, tree_string)
    
    with open(args.treefile, 'w') as tree_file:
        tree_file.write(tree_string)

def replace_string(col_to_check,col, return_string):
    for index,name in enumerate(col_to_check):
        try:
            ## Remove > if it's in conversion file
            if name.startswith(">"):
                name =  name[1:]
            return_string = return_string.replace(name,col[index])

        except:
            print("Could not replace the string, check that your input data is correct")
            import sys
            sys.exit()
    return return_string


if __name__ == "__main__":
    # Command line arguments
    parser = argparse.ArgumentParser("")
    parser.add_argument("-t", "--treefile", required = True, 
    help="Name of treefile that you want to convert")
    parser.add_argument("-c", "--conversion", required = True, 
    help="Name of the table conversion file with your headers")
    
    parser.add_argument("-f", "--from_numb", required = True, default = "1",
    help="Column (number)in the header file that corresponds to the formatyour file is in now")
    parser.add_argument("-to", "--to_numb", required = True, default = "3",
    help="Column (number) in the header file that corresponds to the format that you want it to be")

    args = parser.parse_args()
    main(args)
