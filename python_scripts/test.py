import re

with open('example_data/PCA.txt', 'r') as f:
    text = f.read()
    

pattern = re.compile(r"PCA")
result = pattern.search(text) 
import pdb;pdb.set_trace()

#print("There are {} instances of the word 'PCA' in the wikipedia article about PCA".format(len(result)) )
