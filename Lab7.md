# Sesion 7 - Phylogenetic Analysis

## An introduction to Phylogenetics
Since the eve of Biology as a field of Science, one of the key questions has been how do the different organisms we see today relate to each other, and how they evolved. In the old days we used anatomical similarities (also known as [homologies](https://sites.google.com/site/evidence4evolutiongml/anatomical-homology)) and disimilarities to try to reconstruct their evolutionary history. 
![Example of Homologies](https://sites.google.com/site/evidence4evolutiongml/_/rsrc/1472875637552/anatomical-homology/leah%27s%20pictures.png?height=320&width=867)

With the dawn of genetic sequencing and the genomic era, we can now stablish those relationships with quite more certainty and in a less biased way. Using genetic data for inferring this relationships is known as Philogenetics. 


## Goals
+ Allign our sequences from Session 6 
+ Test which substitution model works better with our data
+ Work with IQTree and learn how to extract information from its output
+ Create a phylogenetic tree meaningful for our porject's question

## Input
+ Fasta sequences of the complete mitochondrial DNA and CytB that we curated on Lab 6

## Output(s)
+ Multiple Allignment of the complete mitochondria
+ Multiple Alligment of the CytB
+ IQTree file with relevant info on out tree
+ Tree file 

## Tools
+ Alignment program: [mafft](https://mafft.cbrc.jp/alignment/software/)
+ Maximum Likelyhood program: [IQTree](http://www.iqtree.org/)

## Details

### Step 1:

The first step before starting anything is be sure that we have the data we need to perform our analysis. So log into Uppmax and navigate to your folder. Now, ask yourself the following questions:

+ Are the species relevant for the question we have to answer? The bigger the distance between species, the longer it will take for everything to run, so be sure you are getting species that are distant enough to be informative but not so much that they slow everything down. 
+ Do I have an appropiate Outgroup to compare them with? This is quite important for the results.
+ Do my sequences have a short and easy to identify header? We want to be able to see easily who is who in our results.

Once we are sure are sure we are ready, the first step is to concatenate our FASTa sequences. If you have them all in their own file, you can do this 


