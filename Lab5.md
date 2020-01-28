# Session 5 - compare with genomes from other species

## Introduction / Background information to Session 5

In this session you will focus on aligments. As you have seen in the lecture, it is possible to align two sequences (pairwise alignments) and multiple sequences (multiple alignments). You will do a bit of both. For the pairwise alignment part, you will follow a tutorial that was developped by Rasmus Wernersson. For the multiple aligments, you will go back to working with the mitochondrial genomes from sessions 3 and 4. You will also work with additional mitochondrial genomes. This will prepare you for the bioinformatic project, as one of the first steps of the project will be to align sequences! Finally, you will write a script that will come in handy for the bioinformatic project.

## Goals

  + Perform local and global pairwise alignments with different algorithms
  + Explore parameters of pairwise alignments
  + Perform multiple alignments with different softwares

## Input(s)

  + Mitochondrial genomes from the following species: XX

## Output(s)

  + An alignment of XX mitochondrial genome
  + A table of mitochondrial features for X genomes
  + Some kind of visual representation of the alignment

## Tools

  + Online alignment tools : https://www.ebi.ac.uk/Tools/psa/
  + Online tool to randomly shuffle a protein sequence: http://www.bioinformatics.org/sms2/shuffle_protein.html

## Steps

  + Start by doing the pairwise alignment exercise.
  + 

## Details

### Pairwise alignment

Please go through the tutorial on this page: http://teaching.bioinformatics.dtu.dk/teaching/index.php/Exercise:_Pairwise_alignment

Questions are numbered from 1 to 14. For the report, you need to submit written answers to the following questions: 9, 11, 14, **more?**.

### Multiple alignment

Step 1: identify the origin of the different fasta files (at least the ones which they have not worked with in the first part) (for example by looking up idenfier or with blast). Identify the odd one. Look up taxonomy information for at least two of the species (prepare bioinformatic project).

Step 2: spend some times on the content of the mitochondrial genomes they are working with (cf annotated genomes on ncbi). Make a summary table for some of the features (we could give the start of the table). What can they expect in the alignments based on that table?

Step 3: create a fasta file with all sequences. Maybe that is the step where they need the script to modify fasta headers?

Step 4: align the sequences. Visualize it. Realize that there is something weird with one of the sequences. Find another sequence for the same species.

Step 5: create a new fasta file, align again. Analyse (point at some interesting aspects). Are the hyp from Step 2 validated?

Possible extra steps: look into colinearity. Include questions which force students to read the program output (e.g. what is printed to screen while the program is running).

### Script to modify fasta headers

The idea of this script is to take a typical NCBI Fasta header and to create a shorter header (a label that can be written easily on a tree). Could also include a step to replace short names with longer names (to make it easier to know what is what on a tree).
