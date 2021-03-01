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

  + FigTree, a phylogenetic tree visualization software

## Details

### Step 1: Examine the IQTree outputs for the mitochondria

In Session 7 you performed a Maximum Likelihood analysis with IQTree on two alignments: *cytB* and entire mitochondria. You answered five questions relative to the *cytB* run. Now, answer these same questions for the mitochondria run. You might be asked about these during the presentation.

**Question 1:** Which files do IQ-TREE output? Explain briefly what each of them is.

Now let's look at the .iqtree file.

**Question 2:** Which model did ModelFinder choose? From all the criteria calculated by this software, which was used to determine the best-fitting model?

**Question 3:** Briefly explain the best-fitting model.

**Question 4:** Now look at both your Maximum Likelihood tree and Consensus Tree. Are they the same? If not, where do they differ?

**Question 5:** In both trees you can see a number at the base of each branch. That is the number of iterations that supported that branching during bootstrapping. Which is your least supported branch? What does that mean to your question?

### Step 2: Create a visual representation of your Maximum Likelihood trees

In the .iqtree file, you have a representation of the trees. However, it is an unrooted tree. You can root the tree, and do many other things, with the program FigTree. You have two options to work with FigTree:

  1. Work locally on the computers from the computer room. In that case, transfer your tree files from Uppmax to the local computer (e.g. using sftp, instructions [here](Troubleshooting_checklist.md)). Then call FigTree with `figtree`.
  2. Work with visual forwarding on Uppmax (log with `ssh -Y`, see [Session 5](Lab5.md). In that case, call FigTree like this: `java -Xms64m -Xmx512m -jar /proj/g2021007/private/SCRIPTS/figtree.jar`
  
When you call FigTree, a visual interface will open. In `File`, choose `Open` and select one of your Maximum Likelihood trees. If the software asks you to select a name for the labels on the tree, you can keep the default or choose a keyword, for example `bootstrap`. **Note that you do *not* want the `.iqtree`, that file is more of a logfile than and actual tree.**

The three important things you have to do are:
  
  1. Root the tree with your outgroup (select the branch and then select `Reroot`)
  2. Show the bootstrap values (using `Branch labels` or `Node labels` and selecting the right thing to display)
  3. Make sure the tree can be easily understood. For example, you might need to change the name of the species, if you are using the short names that you created in [Session 6](Lab6.md). 

You can use this script to change the names in your treefiles:


[treefile\_rename\_from\_conv\_table.py](python_scripts/treefile_rename_from_conv_table.py)
 
Usage example:
 
``` 
python treefile_rename_from_conv_table.py -t CytB_iqTree.treefile -c con_tab_cytb.txt -f 1 -to 3

```

If you are wondering about the options then you can check the help:

```
python treefile_rename_from_conv_table.py -h 
```

_It might also be a good idea to look at the code itself to se how it works, you might learn something ;)_
  

Once you are done with those, you can play around with the other options (for example Rotate & Different type of trees).

**Do not forget to export your trees as `.pdf`. You will have to show them during the presentation.**
  
### Step 3: Reflect on your results

By now you have assembled a dataset to answer the question from Session 6; you collected *cytB* sequences and entire mitochondrial genomes for all species in the dataset; you aligned the species; you perform a Maximum Likelihood analysis with IQTree and looked at some aspects of it, for example the model chosen; and you obtained a visual representation of your rooted trees.

Now it is time to reflect on all that you have done and to answer your phylogenetic question. The preferred method for that is to do it orally during Session 8. If for some reason this is not feasible, you will have to do it in a written form (details for the format are below).

At this stage, you should have two Maximum Likelihood trees: one for *cytB* and one for the entire mitochondria. If you want, you can also look at the consensus trees. To prepare for the presentation, think about:

- What is the answer to the question given these trees?

- Do the different trees give the same answer? If not, what could be the explanation?

- Which tree(s) do you think are most supported? What does the bootstrap analysis tell?

- Are the substitution models different for *cytB* and the entire mitochondria? If yes, what could be an explanation?

- Do you think your choice of species (including the outgroup) was appropriate to answer the question? If you were to redo the analysis, would you change something?


We will also expect you to remind us briefly of the question you worked with, and list which species you chose to include and why, so take a moment to prepare that too.


---
## Presentation

Once you feel like you are ready to present (and not later than one hour before the end of the session), write your names on the board so the teaching assistants can come to listen to you. The presentation will last 5-10 minutes, at your desk.

You do not have to submit anything for this session (if you present orally).

---
## Back-up submission: Written report

In case you could not finish in time, please let the teaching assistants know and submit a written document with your trees (the ones you made with FigTree) and 15-30 lines (or more if you are inspired) answering the questions in **Step 3**. Do not forget to indicate which question you worked with and which species were included in the dataset. Exceptionally one submission by group is allowed - but remember to state the people involved.

---

This is the end of the lab, please make sure that you completed and wrote down the answers to all of the questions.
Upload the **scripts** (code) that you were asked to submit to studium **in the original format** (i.e. .py or .sh), no `pdf` or word files! Any answers that are not code should of course be in text formats such as `.pdf, .txt & .docx`.
Also, make sure to delete any files that you no longer need - you can copy them somewhere else if you want to keep them. This goes for both the Unix computers and Uppmax.

 **Obs!** As this is the last session, this step is extra important. We won't delete anything before March 31 (from the Uppmax project), but afterwards we do not guarantee that the data will be kept. If for some reason you need access to the project after that date, please let the teaching assistants know.
