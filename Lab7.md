# Sesion 7 - Phylogenetic Analysis

## An introduction to Phylogenetics
Since the eve of Biology as a field of Science, one of the key questions has been how do the different organisms we see today relate to each other, and how they evolved. In the old days we used anatomical similarities (also known as [homologies](https://en.wikipedia.org/wiki/Homology_(biology))) and disimilarities to try to reconstruct their evolutionary history. 
![Example of Homologies](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Homology_vertebrates-en.svg/1280px-Homology_vertebrates-en.svg.png)

With the dawn of genetic sequencing and the genomic era, we can now stablish those relationships with quite more certainty and in a less biased way. Using genetic data for inferring this relationships is known as Philogenetics, and it is the "gold-standard" to stablish the relationship between modern species. 

### Base of Phylogenetic Analysis 
Th basic idea behind it all is quite simple: as species diverge over time, they accumulate mutations that the other groups don't share. So, when comparing several sequences, the bigger the number of differences between them, the larger the time since their common ancestor. However, this simple idea gets really complicated quite soon, as we are working with really long sequences and, in some cases, long periods of time. This means that we will need to use robust statistical modelling in order to infer these relationships, that we will represent as a [phylogenetic tree](https://en.wikipedia.org/wiki/Phylogenetic_tree).

![Phylogenetic tree from Ersmark et al. 2016](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Phylogenetic_tree_for_wolves.jpg/468px-Phylogenetic_tree_for_wolves.jpg)

*Phylogenetic tree from Ersmark et al. 2016: https://doi.org/10.3389/fevo.2016.00134*

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
![](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5624502/bin/emss-73449-f001.jpg)

*Prior, likelihood and posterior distribution for a two-parameter phylogenetic example in Nascimento et al. 2017: https://dx.doi.org/10.1038%2Fs41559-017-0280-x*

The last two are the state-of-the-art methods for phylogenetic analysis, and have become more and more popular as computing power has scaled, as both methods are really demanding in that regard. 

For our projects, we are going to use an implementation of the Maximum Likelihood approach called [IQ-TREE](http://www.iqtree.org/doc/Tutorial#first-running-example). This software offers several methods to speed up the analysis. To load the module:

```
module load iqtree/1.6.5-omp-mpi
```
As we mentioned earlier, any Maximum Likelihood approach is based on a model. In phylogenetics, this model describes the probability of each substitution to happen. [Here](http://evomics.org/resources/substitution-models/nucleotide-substitution-models/) you can find a list of the more common models, and [here](http://www.iqtree.org/doc/Substitution-Models) the ones that are implemented in IQ-TREE. 
![Substitution model representation](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fnrg3186/MediaObjects/41576_2012_Article_BFnrg3186_Fig1_HTML.jpg?as=webp)

*GRaphica representation of some substitution models from Yang & Rannala, 2012. Nature Reviews Genetics: https://doi.org/10.1038/nrg3186*

Now that we have a small picture of what we are doing, lets star working with IQ-TREE. The basic syntax for this software is this:

```
iqtree -s ALIGNMENT -o OUTGROUP -m MODEL -pre OUTPUT_PREFIX -bb 1000
```
Now run IQ-TREE in your interactive session with the CytB data, and set your model to *-m MFP*. *MFP* stands for ModelFinder Plus, and algorithm that automatically considers a list of substitution models and estimate which is the one that fits our data better. *-bb 1000* means that we want our algorith to use [bootstraping](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)). **Once the alignment of the whole mitochondrial dataset is done, run IQ-TREE on that dataset via *sbatch*.** Remember to adapt the scritp above to run IQ-TREE (keep the module *bioino-tools*) and be carefull to not over-write your files. 

All the questions bellow refer only to the CytB output.

**Question 1: Which files do IQ-TREE output? Explain briefly what each of them is.** 

Now lets look at the *.iqtree* file. 

**Question 2: Which model did ModelFinder chose? From all the criteria calculated by this software, which was used to determine the best-fitting model?**

**Question 3: Briefly explain the best-fitting model.**

**Question 4: Now look at both your Maximum Likelihood tree and Consensus Tree. Are they the same? If not, where do they differ?** 

**Question 5: In both trees you can see a number at the base of each branch. That is the number of iterations that supported that branching during bootstraping. Which is your least supported branch? What does that mean to your question?**

# REPORT

Submit a file with the answers to all the questions and the *.iqtree* file for the CytB run. 

---

This is the end of the lab, make sure to delete any files that you no longer need - you can copy it somewhere else if you want to keep it. This goes for both the Unix computers and Uppmax.
