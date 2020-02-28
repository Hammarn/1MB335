#!/usr/bin/env python3
import argparse
import pdb

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
               continue
            line = line.rstrip() 
            line =  line.split("\t")
            try:
                col_1.append(line[0])
                col_2.append(line[1])
                col_3.append(line[2])
            except IndexError:
               print("Error: It looks like your conversion table is not properly tab delimited")
               sys.exit() 

    
    if args.to_numb == "1":
        col_to_use = col_1
    elif args.to_numb == "2":
        col_to_use = col_2
    elif args.to_numb == "3":
        col_to_use = col_3

    if args.from_numb == "1":
        tree_string = replace_string(col_1, col_to_use, tree_string, "1")
    elif args.from_numb == "2":
        tree_string = replace_string(col_2, col_to_use, tree_string, "2")
    elif args.from_numb == "3":
        tree_string = replace_string(col_3, col_to_use, tree_string, "3")
    
    with open(args.treefile, 'w') as tree_file:
        tree_file.write(tree_string)

def replace_string(col_to_check,col, return_string, from_number):
    
    for index, old_name in enumerate(col_to_check):
        try:
            ## We don't want to write commas to the treefile since it's used by the viewer 
            if ',' in col[index]:
                col[index] = col[index].replace(',', '')
            ## If there were commas written to the treefile, remove them as well 
            if from_number == "3":
                if ',' in old_name:
                    old_name = old_name.replace(',','') 

            return_string = return_string.replace(old_name,col[index])
            
        except:
            print("Could not replace the string, check that your input data is correct")
            import sys
            sys.exit()
    return return_string


if __name__ == "__main__":
    # Command line arguments
    parser = argparse.ArgumentParser("""Takes a .treefile or .contree from .iqtree or similar and tab delimited conversion table that is assumed to be in the format:
            
            'shortname    longername  longestname'

             """)
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
