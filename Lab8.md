# Session 8 - Wrap-up the bioinformatics project

## Introduction / Background information to session 8

This is the last session of the bioinformatics project (and of the course). You will wrap-up the project and present your results to the teaching assistants (details below).

## Goals

  + Further your understanding of IQTree results
  + Plot trees with a visualization software
  + Answer the question you were given in Session 6
  
## Input(s)

  + The IQTree outputs generated in Session 7
  + The name conversion tables generated in Session 6

## Output(s)

  + .pdf files of your trees

## Tool(s)

  + FigTree, a phylogenetic trees visualization software

## Details

### Step 1: Examine the IQTree outputs for the mitochondria

In Session 7 you performed a Maximum Likelihood analysis with IQTree on two alignments: *cytB* and entire mitochondria. You answered five questions relative to the *cytB* run. Now, answer these same questions for the mitochondria run. You will be asked about these during the presentation.

**Question 1:** Which files do IQ-TREE output? Explain briefly what each of them is.

Now let's look at the .iqtree file.

**Question 2:** Which model did ModelFinder choose? From all the criteria calculated by this software, which was used to determine the best-fitting model?

**Question 3:** Briefly explain the best-fitting model.

**Question 4:** Now look at both your Maximum Likelihood tree and Consensus Tree. Are they the same? If not, where do they differ?

**Question 5:** In both trees you can see a number at the base of each branch. That is the number of iterations that supported that branching during bootstrapping. Which is your least supported branch? What does that mean to your question?

### Step 2: Create a visual representation of your Maximum Likelihood trees

In the .iqtree file, you have a representation of the trees. However, it is an unrooted tree. You can root the tree, and do many other things, with the program FigTree. can You have two options to work with FigTree:

  1. Work locally on the computers from the computer room. In that case, transfer your tree files from Uppmax to the local computer (e.g. using sftp, instructions [here](Troubleshooting_checklist.md)). Then call FigTree with `figtree`.
  2. Work with visual forwarding on Uppmax (log with `ssh -Y`, see [Session 5](Lab5.md). In that case, call FigTree like this: `java -Xms64m -Xmx512m -jar /proj/g2019029/private/SCRIPTS`
  
When you call FigTree, a visual interface will open. In `File`, choose `Open` and select one of your maximum likelihood trees. If the software asks you to select a name for the labels on the tree, you can keep the default or choose a keyword, for example `bootstrap`.

The three important things you have to do are:
  
  1. Root the tree with your outgroup (select the branch and then select Reroot)
  2. Show the bootstrap values (using `Branch labels` or `Node labels` and selecting the right thing to display)
  3. Make sure the tree can be easily understood. For example, you might need to change the name of the species, if you are using the short names that you created in [Session 6](Lab6.md). **Todo write depending on how the script looks like XXXX**  

Once you are done with those, you can play around with the other options (for example Rotate & Different type of trees).
  
**Start here again**  
  
### What was on Sparrman

By now you should have generated all the trees listed here. That's a lot of trees! Now we want you to reflect on the different results and to answer your phylogenetic question. The preferred method for that is to do it orally towards the end of the X9 tutorial (or earlier, when you are done). If for some reason this is not feasible, you will have to do it in a written form.

From all the trees generated in your group, choose two per person (so four in total if your are working in pair) that you find best answer the question. Choose at least one tree from respectively 16S and cytB (so you can have three of one and one of the other but not all of the same). Please think about the strengths of the different methods while you select - the trees can tell different stories but if you can make hypotheses about why they do we will appreciate.

We will expect you to:

-remind us briefly of the question you worked with,

-list which species you chose to include and why,

-present your chosen trees. For each, tell us which trees they are and what they say about your question.

-summarize and conclude (for example, do all trees tell the same story? If not, what could be the explanation? Which trees do you think are the most supported? etc)

This is not a formal presentation (it will last 5-8 minutes in small groups) but if you can have explanatory names on your trees this will help us to follow.


Back-up submission: in case you could not finish in time, please let us know and then submit a written document with your four favourite trees (see above) and write 15-20 lines (or more if you are inspired) about why you chose these trees and how they answer your question. Exceptionally one submission by group is allowed - but remember to state the people involved.




### njplot

Apparently we used njplot to look at the trees with bootstrap.

---
## Presentation:

XXX

---

This is the end of the lab, please make sure that you did and wrote down the answers to all of the questions.
Also make sure to delete any files that you no longer need - you can copy it somewhere else if you want to keep it. This goes for both the Unix computers and Uppmax.