# Session 5 - compare with genomes from other species

## Introduction / Background information to Session 5

In this session you will focus on aligments. As you have seen in the lecture, it is possible to align two sequences (pairwise alignments) and multiple sequences (multiple alignments). You will do a bit of both. For the pairwise alignment part, you will follow a tutorial that was developped by Rasmus Wernersson. For the multiple aligments, you will go back to working with the mitochondrial genomes from sessions 3 and 4. You will also work with additional mitochondrial genomes. This will prepare you for the bioinformatic project, as one of the first steps of the project will be to align sequences! Finally, you will write a script that will come in handy for the bioinformatic project.

## Goals

  + Perform local and global pairwise alignments with different algorithms
  + Explore parameters of pairwise alignments
  + Perform multiple alignments with different softwares

## Input(s)

  + 13 complete mitochondrial genomes
  + 12 sequences for the ribosomal large subunit

## Output(s)

  + An alignment of 12 mitochondrial genome
  + A table of mitochondrial features for 12 genomes
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

#### Step 1: Identify the mitochondrial genomes

Start by login in to Uppmax (rackham). In `/proj/g2019029/private/DATA/session5/Mitochondrial_genomes` you will find 13 complete mitochondrial genomes that were downloaded from NCBI. They are named `Seq1.fasta` to `Seq13.fasta`. Your first task is to identify which species the sequences belong to. Look at the content of the files and think about tools you used in sessions 3 and 4. Once you have identified the species, copy the fasta files which have an incomplete header (for an example of a complete header, see `Seq2.fasta`) to your own directory. Then modify the fasta header with the same information than in `Seq2.fasta` (in particular, sequence identification number and species name). **Should we include example of bash commands? Mention nano or sed?**

**There is an odd sequence. Write down the name of the corresponding fasta file, the species name and the type of sequence. How did you identify it?** 

Possibly: Look up taxonomy information for at least two of the species (prepare bioinformatic project). **todo write**

#### Step 2: Fill a table of mitochondrial features

Before aligning sequences, it is useful to have an idea of how much the sequences might differ. In this case, it is possible to take advantage of the fact that the sequences of interest are well annotated. Complete the following features table for the 12 species. In particular, we are interested in the presence / absence of certain genes and in the length of the mitochondrial genome. **Could they write a script to get the length of the genome? Or simply use wc -c**

**todo start to fill the table below**

Species | Multicellular organism? | Gene x | Gene y | 
 
**Question: what do you learn from this table? What can you expect from the alignment? (make at least two hypotheses)**

#### Step 3: Prepare the input file for the alignment program

Now that you have a better idea of the sequences you are working with, it is time to prepare the input for the alignment program. For that, you will need a fasta file with all sequences. Go ahead and create that file. Remember that some of the files are in `/proj/g2019029/private/DATA/session5/Mitochondrial_genomes` while the rest of the files should be in your own directory. Try to use the command line, for example 

```
cat file1 file2 file2 > threefiles.
```

Now before you proceed with the alignment, you have one more task to do: modify the headers of the fasta file (i.e. the lines starting with `>`). As of now, your headers should look like that:

```
>NC_001328.1 Caenorhabditis elegans mitochondrion, complete genome
```
This is very informative, but having long names and / or cryptic identification numbers will make it difficult for you to identify the sequences when you visualize alignments (and later during the bioinformatic project, when you plot phylogenetic trees). Moreover, some programs (particularly older ones) have a limitation on the number of characters in headers. Your task is thus to write a python script that will shorten the headers; one suggestion of shortened header is:
```
>C_ele_mt
```
You can choose a different format, but keep in mind that it should enable to recognize rapidly the species and also the type of sequence (in this case, the mitochondria).

**Write a script which takes in a fasta file with long headers and outputs a fasta file with shortened headers. Moreover, the script should output a file which has both the long and the short header on the same line, to make sure that it is possible to go back to the long headers. Submit this script.**

Once you have managed the task above, you can delete the fasta file with the long headers, as you can easily recreate it from the separate fasta files and it is redundant with the fasta files with short headers.

#### Step 4: Align the entire mitochondria

Finally, it is time to align your 12 mitochondrial genomes! We are going to use a software called `mafft`. Look for it on rackham. How many versions are available?
```
module spider mafft
```
We will work with version `MAFFT/7.407`.
Aligning this set of mitochondrial genomes is a computationally intensive task. Thus, you should not run anything on the login node! Running heavy processes on the login nodes result in slower performances for everyone, and if you exceed certain limits your processes will be killed. Thus, you should avoid it as much as possibly, either by working in a interactive job or by submitting your jobs through the queue. In the exploratory stage, it is a good solution to work with an interactive job. **To avoid queueing, we asked for reservation for this tutorial. You can login to the reservation using the following command: XXX.** *If we do not have a reservation, ask for interactive job.*
First, load mafft:
```
module load bioinfo-tools MAFFT/7.407
```
Then, just type `mafft`. You will be asked a number of questions, for example: input file name, output file name (include the file extension), output file format, algorithm. For the output file format, choose clustal (sorted) *Or something else depending on what we use for visualization in the end. Other options are: fasta, phylip*. Comment: It might be nice to have two terminal windows open, one with the interactive job and one which you use to navigate to the right folder, check the file names, see whether something gets written to the output etc. For the algorithm, choose `FFT-NS-1 (fast)` *other option that could be relevant: `auto`*. Once you have chosen all the option, the corresponding command-line will be printed to screen.

**Save it and submit it.**

Now, launch the alignment. It will take a while. In the meantime, you can work on the next step, which is another alignment, of a single sequence. It is also a good time to take a break!

#### Step 5: Align the sequence for *16S*

*TODO figure out the corresponding genes for yeast. 16S is part of the 30S subunit (=the small subunit).*

Nowadays there is an abundance of genomic data available, for organelles and for entire genomes, for a large number of species. This is why in this session and in the bioinformatic project, you are aligning the entire mitochondria. However for a long time, it was more common to work with alignment of single genes (and in some cases, for example when exploring the diversity in a given environment, it is still the normal approach). Aligning single genes might also be a good approach when working with diverse species. The 16S ribosomal RNA is - and has been - used a lot in phylogenetic inferences, as it is a slowly evolving. *Name in yeast?*
In folder `/proj/g2019029/private/DATA/session5/XXX` you will find 12 fasta files, corresponding to the sequence of interest for the same 12 species than in the previous steps. Prepare the alignment input in the same way: create a fasta file with the 12 sequences and change the headers to short ones (remember to modify the part of the short header about the type of sequence). Now, proceed to the alignment with `mafft`. You can take the same command like the one you created when submitting the alignment for the entire genome - remember to modify the input and output file name. Submit it as a job like this - replace YOURCOMMAND, and youremailforUppmax:

```
(echo '#!/bin/bash -l'
echo '
module load bioinfo-tools MAFFT/7.407
YOUR COMMAND
exit 0') | sbatch -p core -n 1 -t 15:00 -A g2019029 -J align_rRNA -o align_rRNA.output -e align_rRNA.output --mail-user youremailforUppmax --mail-type=END,FAIL
```

You will receive an email when the job finishes (or fails). What normally would have been printed to the screen will be printed to align_rRNA.output. Have a look at it! *Ask them to get some information from that?*

Now, have a look at the alignment *Still need to decide how they will do that*. What do you see? Normally one of the sequences should stand out. **Which one?**

#### Step 6: Find a new *16S* sequence and align one more time

The strange alignment from Step 5 is a genuine example, that was discovered by students who took this course previously. It results from a mis-annotation in the reference mitochondrial genome for the cheetah. A new genome, with the proper annotation, was submitted.

**Find the *16S* sequence for AY463959.1. Perform the alignment again (see Step 5). Visualize it. Is the issue solved? Show it to a teaching assistant.**

The main take-home message from this step is that it is important to examine well your alignments. Sometimes some sequences will genuinely be longer or shorter than other sequences; however it might also be due to some errors!

#### Back to step 4

By now the alignment of the entire mitochondria should be ready for you to look at! Open it in a visualization program. What do you see? Does it match your expectations after filling the feature table?

**Do you think that it was meaningful to align these 12 mitochondrial genomes? Would you remove some if you were to do it again? Which?** *Other questions?*


*Possible extra steps: look into colinearity. Include questions which force students to read the program output (e.g. what is printed to screen while the program is running). Play with alignment options. Use another alignment software.*

