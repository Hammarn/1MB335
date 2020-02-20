# Sesion 7 - Phylogenetic Analysis

## An introduction to Phylogenetics
Since the eve of Biology as a field of Science, one of the key questions has been how do the different organisms we see today relate to each other, and how they evolved. In the old days we used anatomical similarities (also known as [homologies](https://en.wikipedia.org/wiki/Homology_(biology))) and disimilarities to try to reconstruct their evolutionary history. 
![Example of Homologies](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Homology_vertebrates-en.svg/1280px-Homology_vertebrates-en.svg.png)

With the dawn of genetic sequencing and the genomic era, we can now stablish those relationships with quite more certainty and in a less biased way. Using genetic data for inferring this relationships is known as Philogenetics, and it is the "gold-standard" to stablish the relationship between modern species. 

### Base of Phylogenetic Analysis 
Th basic idea behind it all is quite simple: as species diverge over time, they accumulate mutations that the other groups don't share. So, when comparing several sequences, the bigger the number of differences between them, the larger the time since their common ancestor. However, this simple idea gets really complicated quite soon, as we are working with really long sequences and, in some cases, long periods of time. This means that we will need to use robust statistical modelling in order to infer these relationships, that we will represent as a [phylogenetic tree](https://en.wikipedia.org/wiki/Phylogenetic_tree).

![Phylogenetic tree from Ersmark et al. 2016](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Phylogenetic_tree_for_wolves.jpg/468px-Phylogenetic_tree_for_wolves.jpg)

Each tree is a hypothesys of the relationship between our sequences, and our goal is to identify, from all the posible trees, the one that is most likely to be true according to our data. This may vary depending on the region you are looking at, the models that you use or how you preprocess and allign your sequences. 

So, with this in our minds, lets get going. 

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

Once we are sure are sure we are ready, the first step is to concatenate our FASTa sequences. If you have them all in their own folder, you can do this like this:

```
cat *.fasta > 
```



