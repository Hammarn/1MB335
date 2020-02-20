# Sesion 7 - Phylogenetic Analysis

## An introduction to Phylogenetics
Since the eve of Biology as a field of Science, one of the key questions has been how do the different organisms we see today relate to each other, and how they evolved. In the old days we used anatomical similarities (also known as [homologies](https://en.wikipedia.org/wiki/Homology_(biology))) and disimilarities to try to reconstruct their evolutionary history. 
![Example of Homologies](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Homology_vertebrates-en.svg/1280px-Homology_vertebrates-en.svg.png)

With the dawn of genetic sequencing and the genomic era, we can now stablish those relationships with quite more certainty and in a less biased way. Using genetic data for inferring this relationships is known as Philogenetics, and it is the "gold-standard" to stablish the relationship between modern species. 

### Base of Phylogenetic Analysis 
Th basic idea behind it all is quite simple: as species diverge over time, they accumulate mutations that the other groups don't share. So, when comparing several sequences, the bigger the number of differences between them, the larger the time since their common ancestor. However, this simple idea gets really complicated quite soon, as we are working with really long sequences and, in some cases, long periods of time. This means that we will need to use robust statistical modelling in order to infer these relationships, that we will represent as a [phylogenetic tree](https://en.wikipedia.org/wiki/Phylogenetic_tree).

![Phylogenetic tree from Ersmark et al. 2016](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Phylogenetic_tree_for_wolves.jpg/468px-Phylogenetic_tree_for_wolves.jpg)

*Phylogenetic tree from Ersmark et al. 2016: 10.3389/fevo.2016.00134*

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

For this Session we are going to use the files that we created in the previous one. Make sure you followed the instructions properly and that you have all the files located. 

### Step 1a:

The first step is to do a Multiple Alignment. As our mitochondrial sequences are considerably bigger than the single gene ones, we will submit them as an independent job to Rackham, as we did in Session 5. However, today we are going to use the other method to submit a job using *sbatch*: an scritp. It should look like this:
```
#!/bin/bash -l
#SBATCH -A g2019029
#SBATCH -p core
#SBATCH -n 1
#SBATCH -t 45:00
#SBATCH -J align_mt 
#SBATCH -o align_mt.output 
#SBATCH -e align_mt.output 
#SBATCH --mail-user youremailforUppmax 
#SBATCH --mail-type=END,FAIL

module load bioinfo-tools MAFFT/7.407

YOUR MAFFT COMMAND
exit 0
```

Now look at the *SBATCH* bits. Look familiar? Yes, they are the same (almost) parameters that we used in Session 5, but this time we are imputing them inside the script, instead of specifying them when we call *sbatch*. Remember to change *youremailforUppmax* and * YOUR MAFFT COMMAND* for your own email and command, respectively.

Now, in order to submit the job, just use this code:

```
sbatch SCRIPT_NAME
```

If you want to check that your job has been submited and in which state it is, use this command:
```
jobinfo -u YOUR_UPPMAX_USER
```

### Step 1b:

Now open an interactive session and do the same with your CytB sequences. 

### Step 3:

Once we have the alingment, we can get to infering which of all the posible trees is the most likely. We have several methods to do this:

+ [Parsimony](https://www.mun.ca/biology/scarr/2900_Parsimony_Analysis.htm): "the simplest explanation that can explain the data is to be preferred", so the hypothesis with the smallest number of changes is the most likely. However, this method have plenty of assumptions that we know are false, so it is not used anymore.
+ [Neighbour-joining](https://academic.oup.com/mbe/article/4/4/406/1029664): Slightly more refined version of parsimony in which we chose the best tree by minimizing branch lengths in the tree. More computationaly intensive than parsimony, but still something that a modern computer can do fairly quick.
+ [Maximum Likelihood](http://ib.berkeley.edu/courses/ib200a/lect/ib200a_lect11_Will_likelihood.pdf): "Likelihood is defined to be a quantity proportional to the probability of observing the data given the model". This means that, by providing a model of how DNA sequences change, we can determine which tree is the most probable to be true. 
+ [Bayesian Inference](https://www.sciencemag.org/site/feature/data/1050262.pdf): This method uses Bayesian Statistics to combine prior information that we know about our data (also known as Prior Probability Distribution) with the likelyhood, in order to transform it into a more accurate probability distribution, known as the Posterior.
![](https://www.ncbi.nlm.nih.gov/corecgi/tileshop/tileshop.fcgi?p=PMC3&id=749074&s=71&r=1&c=3)

*Prior, likelihood and posterior distribution for a two-parameter phylogenetic example in Nascimento et al. 2017: https://dx.doi.org/10.1038%2Fs41559-017-0280-x*

