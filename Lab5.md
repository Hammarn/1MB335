# Session 5 - Alignments of mitochondrial sequences

## Introduction / Background information to Session 5

In this session you will focus on alignments. As you have seen in the lecture, you can align two sequences (pairwise alignment) or multiple sequences (multiple alignment). Today, you will do a bit of both. For the pairwise alignment part, you will follow a tutorial that was developped by Rasmus Wernersson. For the multiple alignment part, you will continue to work with the mitochondrial genomes from Sessions 3 and 4. You will also work with additional mitochondrial genomes. This will prepare you for the bioinformatic project, as one of the first steps of the project will be to align sequences.

## Goals

  + Perform local and global pairwise alignments with different algorithms
  + Explore parameters of pairwise alignments
  + Perform multiple alignments and visualize them
  + Manipulate files

## Input(s)

  + complete mitochondrial genomes
  + sequences for the ribosomal large subunit (l-rRNA)

## Output(s)

  + An alignment of mitochondrial genomes
  + Two alignments of the ribosomal large subunit

## Tools

  + [Online alignment tools](https://www.ebi.ac.uk/Tools/psa/)
  + [Online tool to randomly shuffle a protein sequence](http://www.bioinformatics.org/sms2/shuffle_protein.html)
  + Alignment program: [mafft](https://mafft.cbrc.jp/alignment/software/)
  + Alignment visualization program: clustalw / clustalx

## Steps

  + Step 1: Pairwise alignment exercise
  + Step 2: Multiple alignment exercise
    + Step 2a: Identify the mitochondrial genomes
    + Step 2b: Make a prediction about the alignment
    + Step 2c: Prepare the input file for the alignment program
    + Step 2d: Align the entire mitochondria
    + Step 2e: Align the sequence for the large mitochondrial ribosomal RNA (l-rRNA)
    + Step 2f: Find a new l-rRNA sequence and align one more time

## Details

### Step 1: Pairwise alignment

Please go through the tutorial on [this page](http://teaching.bioinformatics.dtu.dk/teaching/index.php/Exercise:_Pairwise_alignment).

Questions are numbered from 1 to 14. Submit answers to all the questions (you can number them 1-1, 1-2 etc to distinguish them from the answers to the next part).

### Step 2: Multiple alignment

#### Step 2a: Identify the mitochondrial genomes

Start by login in to Uppmax (rackham). In `/proj/g2019029/private/DATA/session5/Mitochondrial_genomes/` you will find 14 complete mitochondrial genomes that were downloaded from NCBI. They are named from `Seq1.fasta` to `Seq14.fasta`. Copy all the files to your own directory.

Your first task is to identify which species the sequences belong to. Look at the content of the files and think about tools you used in sessions 3 and 4. Once you have identified the species, complete the headers of the files which have an incomplete header (for an example of a complete header, see `Seq2.fasta`): they should have the same information than in `Seq2.fasta` (in particular, sequence identification number and species name).

Hint: you can use `nano` to modify files in the command line.

**Question 1. To which species do the different sequences belong to?** 

**Question 2. There is an odd sequence. Write down the name of the corresponding fasta file, the species name and the type of sequence. How did you identify it?**

How much do you know about the species that are in the dataset? Do you know how they are related? To start to answer these questions, [Wikipedia](https://en.wikipedia.org/) and the [taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Root) (yet another NCBI tool!) are very helpful.

Start by looking up the species from Seq4 in Wikipedia. Which family does it belong to? (see the box on the right) Now, go to the taxonomy browser and look for that same species. One of the item on the page is the full "lineage" of that species, from the widest to the most specific category. Find the family name and click on it.

**Question 3. What is the common name of this family of species? Which other species from the dataset belong to that same family? Perform the same thing (and answer the second part of the question) with species from Seq14.**

Before you continue, look up quickly the species that you don't know about in wikipedia (or the tool you prefer).

#### Step 2b: Make a prediction about the alignment

Before aligning sequences, it is useful to have an idea of how much the sequences might differ. Have a look at Figure 3 in the review 'The Origin and Diversification of Mitochondria' Roger et al., Current Biology Review 2017 (you can find the review on Studentportalen, under Bioinformatics/Computer labs). Focus on the 'Opisthokonta'. You won't find information for all the species in the dataset - in particular, the only representative of the Metazoa (animals) in the table is 'Homo'. Look at the absence / presence of genes in these different mitochondrial genomes.
 
**Question 4. What do you learn from this table? What can you expect from the alignment? (make at least one hypothesis)**

Another thing that is not visible in the figure from the review but which will impact your alignment is the length of the mitochondrial sequences.

#### Step 2c: Prepare the input file for the alignment program

Now that you have a better idea of the sequences you are working with, it is time to prepare the input for the alignment program. For that, you will need a fasta file with all the **mitochondrial** sequences. Try to use the command line: You can do it as below (or in a smarter way using `*` if you remember)

```
cat file1 file2 file2 > threefiles
```

Before you proceed with the alignment, you have one more task to do: modify the headers of the fasta file (i.e. the lines starting with `>`). As of now, your headers looks something like this:

```
>NC_001328.1 Caenorhabditis elegans mitochondrion, complete genome
```
This is very informative, but having long names and / or cryptic identification numbers will make it difficult for you to identify the sequences when you visualize alignments (and later during the bioinformatic project, when you plot phylogenetic trees). Moreover, some programs (particularly older ones) have a limitation on the number of characters in headers. You should thus shorten the headers before you proceed further (for example with the text editor `nano`). One suggestion of shortened header is:

```
>C_ele_mt
```
You can choose a different format, but keep in mind that it should enable to recognize rapidly the species and also the type of sequence (in this case, the mitochondria). If you want to write a script to do this instead of using a text editor, see **Optional**.

Once you have managed the task above, you can delete the fasta file with the long headers, as you can easily recreate it from the separate fasta files and it is redundant with the fasta files with short headers.

---
**Optional:** Alternatively, you can write a Python script that will shorten the headers. For example, it could be a script which takes as input a fasta file with long headers and outputs a fasta file with shortened headers. Moreover, the script should output a file which has both the long and the short header on the same line, to make sure that it is possible to go back to the long headers.

---

#### Step 2d: Align the entire mitochondria

Finally, it is time to align your **13 mitochondrial** genomes! We are going to use a software called `mafft`. Look for it on rackham. How many versions are available?
```
module spider mafft
```
We will work with version `MAFFT/7.407`.

Reminder about computation on Uppmax: Aligning this set of mitochondrial genomes is a computationally intensive task. Thus, you should not run anything on the login node! Running heavy processes on the login nodes result in slower performances for everyone, and if you exceed certain limits your processes will be killed. Thus, you should avoid it as much as possibly, either by working in a interactive job or by submitting your jobs through the queue. In the exploratory stage, it is a good solution to work with an interactive job. **To avoid queueing, we asked for reservation for this tutorial.**

For the course on February 17, the reservation is: g2019029_17

For the course on February 19, the reservation is: g2019029_19

Ask for an interactive session with the following command (replace "name_of_reservation" by either g2019029_17 or g2019029_19):

```
interactive -A g2019029 -p core -n 1 -t 4:0:0 --reservation=name_of_reservation
```

Now, load mafft:
```
module load bioinfo-tools MAFFT/7.407
```
Then, just type `mafft`. You will be asked a number of questions, among others: input file name, output file name (include the file extension, `.clustal` in this case), output file format, algorithm. For the output file format, choose clustal (sorted). For the algorithm, choose `FFT-NS-1 (fast)`.

Comment: It might be nice to have two terminal windows open, one with the interactive job and one which you use to navigate to the right folder, check the file names, see whether something gets written to the output etc.

Once you have chosen all the options, the corresponding command-line will be printed to screen.

**Question 5. Write down the command.**

Now, launch the alignment. It will take a while. In the meantime, you can work on the next step, which is another alignment, of a single gene. It is also a good time to take a break!

#### Step 2e: Align the sequence for the large mitochondrial ribosomal RNA (l-rRNA)

Nowadays there is an abundance of genomic data available, for organelles and for entire genomes, for a large number of species. This is why in this session and in the bioinformatic project, you are aligning the entire mitochondria. However for a long time, it was more common to work with alignments of single genes (and in some cases, for example when exploring the diversity in a given environment, it is still a common approach). Aligning single genes might also be a good approach when working with diverse species. And of course, it is much faster!

The  large mitochondrial ribosomal RNA (l-rRNA) which is part of the large subunit of the ribosome (in the mitochondria) is - and has been - used a lot in phylogenetic inferences, as it is a slowly evolving. Depending on the species you are working with, this RNA might have different names, for example 16S, rnl, l-RNA, 21S etc.

For this step, we will focus on the multicellular eukaryotic organisms ('Metazoans') in our dataset. In folder `/proj/g2019029/private/DATA/session5/Ribosomal_large_subunit` you will find seven fasta files, corresponding to the sequence of interest for seven of the species from the previous step. Start by finding the corresponding sequence for three extra species: Seq8, Seq9, and Seq14 (go to NCBI, find the annotated mitochondria, and look for rRNA; be careful, there are two rRNA per mitochondrial genome! Choose the larger one). We will not use the other genomes for this and the following step.

Then, prepare the alignment input in the same way like in Step 2c: create a fasta file with the 10 sequences and change the headers to short ones (remember to modify the part of the short header about the type of sequence). Now, proceed to the alignment with `mafft`. You can take the same command like the one you created when submitting the alignment for the entire genome - remember to modify the input and output file name. Submit it as a job like this - replace YOURCOMMAND, and youremailforUppmax:

```
(echo '#!/bin/bash -l'
echo '
module load bioinfo-tools MAFFT/7.407
YOUR COMMAND
exit 0') | sbatch -p core -n 1 -t 15:00 -A g2019029 -J align_rRNA -o align_rRNA.output -e align_rRNA.output --mail-user youremailforUppmax --mail-type=END,FAIL
```

You will receive an email when the job finishes (or fails). What normally would have been printed to the screen will be printed to align_rRNA.output. Have a look at it!

Look at the output file (the .clustal). Do you understand the format?

In order to have a better overview of the alignment, we are going to use the `clustalw` program. Using a program with visual forwarding like this one involves a different kind of connection to Uppmax. Open a new tab in your terminal and type:

```
ssh -Y your_user_name@rackham.uppmax.uu.se
```

**If you are using a Mac** , then you first need to install `Xquartz`: 

[https://www.xquartz.org/](https://www.xquartz.org/)


Like when you loaded `mafft`, look for the versions of `clustalw` installed on rackham and load the module.

**Question 6. Which version of `clustalw` did you load?**

`clustalw` can perform alignments. However, we already have an alignment and are only interested in the visualization part. The following command will open an interface - we add a `&` in the end, as this enables you to continue to use the command-line while having the interface opened.

```
clustalx &
```
In "File", choose "Load Sequences" and choose your alignment. Can you make sense of what you see? What do you think the bottom window shows?

**Question 7. Normally one of the sequences should stand out. Which one?**

#### Step 2f: Find a new l-rRNA sequence and align one more time

The strange alignment from Step 2e is a genuine example, that was discovered by students who took this course previously. It results from a mis-annotation in the reference mitochondrial genome for the cheetah. A new genome, with the proper annotation, has been submitted since then.

Find the *16S* sequence for the mitochondrial genome with identifier AY463959.1. Perform the alignment again (see Step 2e). Visualize it. Is the issue solved? 

**Question 8. Show your new alignment to a teaching assistant. If you cannot show it, submit the corresponding alignment.**

The main take-home message from this step is that it is important to examine your alignments well. Sometimes some sequences will genuinely be longer or shorter than other sequences; however it might also be due to some errors!

#### Back to Step 2d

By now the alignment of the entire mitochondria should be ready for you to look at! Open it with `clustalx` (see Step 2f). What do you see? Does it match your expectations after filling the feature table?

**Question 9. Do you think that it was meaningful to align these 13 mitochondrial genomes? Would you remove some if you were to do it again? Which?**

---
## REPORT

Pairwise alignment tutorial: submit answers to all questions (you can number them 1-1, 1-2 etc).

Multiple alignment: submit answers to questions 1 through 9 (you can number them 2-1, 2-2 etc). For Question 9, submit the alignment only if you could not show it to a teaching assistant.

Please specify if you did the tutorial on February 19!

---

This is the end of the lab, make sure to delete any files that you no longer need - you can copy it somewhere else if you want to keep it. This goes for both the Unix computers and Uppmax.
