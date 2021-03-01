# Session 4 - annotate your mitochondrial genome

## Introduction / Background information to Session 4
  
During Session 3, you went through the steps to assemble a circular mitochondrial genome; finally, you orientated it. In this session you will make sense of the sequence. The mitochondrial genome, like the nuclear genome, codes for proteins, transfer RNA (tRNA) and ribosomal RNA (rRNA). These elements are necessary for the function of the mitochondria. For example, the proteins are involved in ATP synthesis and protein synthesis; the tRNA are necessary for the translation from RNA to protein; and the rRNA are necessary to assemble the ribosomes. Other elements also necessary for the mitochondria to function are coded for in the nuclear DNA.

'Annotation' means finding the location of the different elements in the genome. This can be done in different ways. For example, one can look for conserved sequences between different species. It is also possible to predict the location of protein coding genes by searching for start codons (such as ATG - remember the part about *cox1* in Session 3) and promoters. Once you have annotated the genome and know where a given gene is, it is easy to extract that gene and e.g. use it for comparative approaches (Session 5) or to build phylogenies (like you will do in the bioinformatics project: Sessions 6-8).

Because you are working with close relatives of model organisms, it will be quite easy to annotate the mitochondrial genome. However, you could follow the same steps if you were working with non-model organisms.

The text from this session is modified from "A guide to organellar genome assembly and annotation", by Cloe Pogoda, Kyle Keepers, and Nolan Kane, the accompanying document of "A CURE-based approach to teaching genomics using mitochondrial genomes", CS Pogoda et al, CourseSource 2019.

## Goals

+ Annotate a mitochondrial genome.
+ Get familiar with some of the features of the mitochondria.
+ Get familiar with some annotation tools.
+ Continue to program in Python.

## Input(s)

+ the circularized, orientated mitochondria for your species of interest (format: fasta), from Session 3.

## Output(s)

+ an annotated mitochondrial genome for your species of interest.
+ a graphical representation of the genome.
+ a Python script.

## Tools

+ [GeSeq software](https://chlorobox.mpimp-golm.mpg.de/geseq.html)
+ [tRNAscan software](http://lowelab.ucsc.edu/tRNAscan-SE/)
+ web-based blast
+ [OGDraw software](https://chlorobox.mpimp-golm.mpg.de/OGDraw.html)
+ [ORFfinder](https://www.ncbi.nlm.nih.gov/orffinder/)

## Steps

+ Step 1: Perform a first annotation with GeSeq
+ Step 2: Complete the annotation of tRNAs with tRNAscan
+ Step 3: Use web-based blast to confirm features boundaries
+ Step 4: Use web-based blast to improve the annotation of rRNA
+ Step 5: Draw a visual representation of your annotated mitochondria and identify unannotated regions
+ Step 6: Look for open reading frames with ORF finder
+ Step 7: A bit of programming

## Details

### Step 1: Perform a first annotation with GeSeq

Open [GeSeq](https://chlorobox.mpimp-golm.mpg.de/geseq.html) in your browser.
On the left hand side of the page under 'FASTA file(s) to annotate' click 'Upload files', and select the appropriate file (your COX1 reoriented .fasta file from Session 3).

Next, click the appropriate boxes to indicate that this is a circular genome and select the correct sequence source (**mitochondrial**). We suggest leaving the rest of the options available on the left hand side at their default settings. 

Next, in the middle section of the page under “BLAT Reference Sequences” click “Add NCBI refseq(s)” which will open a new tab where you can select species that are similar to the one you are annotating (closely related species are the best). Refer to the table in Session 3 to know which species to choose. Leave the rest of the options in the middle section unselected. 
 
Then, click the button to indicate you have read the disclaimer and hit “Submit”. The program should only take a few moments to run and will produce several files. We are currently interested in downloading the GenBank file.


Next, **open this file in your text editor** and take a look at the file produced.  We suggest you look for duplicated entries in your file. GeSeq uses multiple references and depending on how the researcher’s annotated their genomes there might be features named rps3 and RPS3 (for example), both of which are the same feature but GeSeq treats them as separate. Go ahead and delete any redundant features that are duplicated, as again, this is the easiest stage of the annotation to perform this action. You might notice that you have gene, CDS, exon and intron lines for a given feature (i.e., cox1). **Delete any lines that say exon and intron, if there are any** and only save the lines that contain information for gene, CDS, tRNA or rRNA. If you were to submit your annotation to NCBI, having all of these duplicated entries would be causing issues.

This is a list of the features that are most likely present in your mitochondrial genome. Sometimes the names of the genes might differ (for example for the rRNA). In that case you can google or search on NCBI before asking the teaching assistants. Depending on your species all or very few of them might be present at this stage.

***Table 1. Features of the mitochondrial genome.***

tRNA | genes | rRNA
--|--|--
Ala (A) | ATP6 | s-RNA
Arg (R) | ATP8\** | l-RNA
Asn (N) | COX1 |
Asp (D) | COX2 |
Cys (C) | COX3 |
Gln (Q) | CYTB |
Glu (E)| ND1 |
Gly (G) | ND2 |
His (H) | ND3 |
Ile (I) | ND4 |
Leu\* (L) | ND4L |
Lys (K) | ND5 |
Met (M) | ND6 |
Phe (F)
Pro (P)
Ser\* (S)
Thr (T)
Trp (W)
Tyr (Y)
Val (V)

\* These tRNA might be present twice as two different codons can be translated into these amino acids.

\** The gene *ATP8* is not present in the mitochondria of Caenorhabditis remanei.

**Question 1. How many of these features are found by GeSeq?**

### Step 2: Complete the annotation of tRNAs with tRNAscan

To find tRNAs, GeSeq uses the program tRNAscan (Lowe & Eddy 1997). To ensure we have found all of the tRNAs, it is best to double check the lengths and identities of the tRNAs found in GeSeq by using the stand alone tRNAscan program, which has a very easy to use web interface. The program may be found [here](http://lowelab.ucsc.edu/tRNAscan-SE/). In the proper dialog box upload your sequence, change the dropdown box for 'Sequence source' to the right answer for your species and leave everything else as default. Hit submit.

Obs! tRNAscan is a bit annoying with formatting and might complain about the header of your fasta file (for example). In that case, copy your original fasta file and simplify the header before resubmitting. You can also paste the sequence in the search box, if you leave out the header you have to instead click on "Raw sequence" instead of "Formated fasta file".

After a short while, you will see a list of the tRNAs and their locations in your genome. Compare these results to what GeSeq found and note if anything is missing or locations are divergent. Refer to the table below for a list of all the amino acids that should be present in your genome and for any conversion that you need to make (more details after Question 2).
Note that depening on your organizm tRNA-Scan might find 3-25 different tRNAs.

***Table 2. Amino acid names translation table.***

Long name | tRNA name | One letter code
--|--|--
Alanine | Ala | A
Cysteine | Cys | C
Aspartic acid | Asp | D
Glutamic acid | Glu | E
Phenylalanine | Phe | F
Glycine | Gly | G
Histidine | His | H
Isoleucine | Ile | I
Lysine | Lys | K
Leucine | Leu | L
Methionine | Met | M
Asparagine | Asn | N
Proline | Pro | P
Glutamine | Gln | Q
Arginine | Arg | R
Serine | Ser | S
Threonine | Thr | T
Valine | Val | V
Tryptophan | Trp | W
Tyrosine | Tyr | Y

**Question 2. How many tRNAs were identified? Were they already identified by GeSeq? Do the coordinates differ between the two softwares? If yes, write the two sets of coordinates down. Which do you think are the correct coordinates?**

To answer the last question, you can go to the NCBI page of the annotated genome. You can look for example at the length of the tRNA. You can also try to compare directly the coordinates, but because you are working with a genome orientated with *cox1* you will need to shift the coordinates.

If tRNAscan identified features that GeSeq did not find, add them to the GeSeq output as follow: For example, let’s say that tRNAscan found the tRNA for tyrosine, which GeSeq did not find. We will need to add it in the GeSeq output. tRNAscan will use the three-letter code "tyr", we see from our translation table that the one letter code is Y (Table 2). In addition, we see in tRNAscan output that the anti-codon for tyrosine is GTA. Therefore, the correct format for the gene name will be “trnY-GUA” (all T’s become U’s because we are dealing with RNA not DNA, and "trn" stands for tRNA). Refer back to tRNAscan for the boundaries of this tRNA. In the GenBank formatted text file enter the missing tRNAs using the same format as presented for the tRNAs that GeSeq did find.


*Note: If you are adding something from a source that does not privide a score (such as tRNA scan) then you of course don't have to add a score line.*

### Step 3: Use web-based blast to confirm features boundaries

The boundaries (i.e. start and end) identified by GeSeq for the different features might not be accurate. One way to verify the accuracy of the boundaries is to perform a blast. For that, you need to navigate to the GenBank entry of your close relative or reference (see Table 1 in Session 3 if you do not remember!). 

GenBank is the default format of the NCBI entry, e.g. [here](https://www.ncbi.nlm.nih.gov/nuccore/NC_001328.1) for Caenorhabditis elegans). In the top right of your reference’s GenBank page is a dropdown box titled 'send'. Click on this and select 'coding sequences' in .fasta protein format, this will open the file on your computer. The file contains the amino acid sequence of all the protein coding features of your reference. We will use these sequences to finalize the boundaries of the protein features that we have imported from GeSeq by BLASTing the reference sequence against your own.We will  start by verifying the boundaries of *cox2*. This is similar to the work you did in Session 3 with *cox1*.

#### Here are the instructions for *cox2*:

Open the `blastx` page of NCBI and select 'Align two or more sequences'. Within the text file you just downloaded from NCBI, search for the string “cox2” and copy the amino acid sequence for this gene. Return to your blastx window. Now paste your copied *cox2* sequence into the bottom of the two dialog windows. Now either paste in or upload your `.fasta` sequence into the top dialog window. _Note that we chose a file rather than pasting a nucleotide sequence into the window_. Also, **note that you must choose the correct genetic code, otherwise your results will be inaccurate**. This will vary according to the taxon and the locus. Depending on your species, you will choose from: 

* Vertebrate mitochondrial
* Invertebrate mitochondrial

You can find more information about the different genetic code on this [wikipedia page](https://en.wikipedia.org/wiki/List_of_genetic_codes) (which suggests the alternative code 14 for nematodes - those of you working with nematodes can go ahead and try!).

Also, choose 'Show results in a new window' - this will allow you to change parameters more easily if you need to. Now, submit the blast. Go to the 'Dot plot' tab. If you have one solid large line spanning the entire vertical span (or most) of the dot matrix that is an indicator that the gene is complete and in one exon. Then look at the 'Alignments' tab.

**Question 3. Is the gene complete and in one exon? If not, how does it look like? About the alignment: what is the first amino acid position of the reference ('Sbjct') which align well to your mitochondrial genome?**

If the first amino acid position which aligns well to the reference is not 1, it could be that the start amino acid (usually a methionine) is upstream of the corresponding position in your mitochondrial genome. Have a look at your mitochondrial genome and try to find a start codon (ATG is the most common, but other are possible: ATA, ATT, etc - you can check the wikipedia article mentioned above). Look at the end of the alignment too. Does it correspond to the end position inferred by GeSeq? (there might be a difference due to incorporating or not the stop codon)

Now, choose one more gene from the list of coding sequences that you downloaded for your reference genome and repeat the steps you just performed for *cox2*.

**Question 4. Which gene did you choose? Does it have one or several exons? Do the boundaries match with the GeSeq boundaries? If not, list the GeSeq and the blast boundaries. Does the alignment start at position 1 of the subject? If not, make an hypothesis concerning the location of the start codon in your own genome.**

### Step 4: Use web-based blast to improve the annotation of rRNA

There are two rRNA genes in the mitochondria, a short and a long one. They are part of the assembly of the ribosomal sub-units (and the ribosomes are the structure responsible for protein synthesis). They are also very useful for phylogenetic studies, and we will work more with them in Session 5.

GeSeq is not very efficient at localizing the location of rRNA, and at the moment there are no other good tools to annotate rRNA. Thus you will proceed like in Step 3, but this time you will use blastn because your "subject" sequence is in nucleotides not amino acids.

In short: go to NCBI, find the sequence for the long rRNA gene in your reference genome (the name might differ: l-rRNA, rnl, 16S). Perform a blastn between your study species (query) and your reference genome (subject). Look at the dot plot and the alignments.

**Question 5. Do the coordinates differ between GeSeq output and what blastn suggests?**

If you trust the blastn result more, update the start and end coordinates in the GeSeq output. Good reasons to trust the blastn output is if GeSeq predicted the genes to be in several pieces; or if the genes predicted by GeSeq were very short (less than 500 base pairs would be short).

### Step 5: Draw a visual representation of your annotated mitochondria and identify unannotated regions

It would be nice to be able to visualize the result of your hard work, isn't it? Luckily, there is a tool that will do just that. Go to [OGDraw software](https://chlorobox.mpimp-golm.mpg.de/OGDraw.html). Make sure to set the `Sequence source` as Mitochondria!
Upload your GeSeq output (which you should have updated in steps 2, 3 and 4). Check "Show full legend" in Map Options, and choose "PDF" as output format. Submit!

**Question 6. Now, look at the output. Do you see regions devoid of annotated features? See the example below (Figure 1).**

![](Figures/Figure_gap_in_OGDrawoutput_Pogodaetal.png)

**Figure 1: An example output of OGDraw with a gap.** *The black arrow indicates a gap in annotated features where undiscovored proteins may exist. Taken from Pogoda et al. A guide to organellar genome assembly and annotation.*

If you do see gaps of > 300 base pairs, write down the coordinates (you can for example look at the coordinates of the features on both ends of the gap) and proceed to the next step. Should you have no gap at all, save the output of OGDraw (you will need to submit it).

### Step 6: Look for open reading frames (ORF) with ORFfinder

We are going to use a last annotation tool, [ORFfinder](https://www.ncbi.nlm.nih.gov/orffinder/), to find putative genes (open reading frames). In particular, we are going to investigate the gaps that you identified in Step 6. If you did not identify any gap, you can perform the analysis on the entire mitochondria.

Go to [ORFfinder](https://www.ncbi.nlm.nih.gov/orffinder/) and copy your mitochondrial sequence. In Search parameters, choose 300 for the minimal ORF length, as it is unlikely that protein coding genes will be shorter than 300 base pairs. You also need to specify the genetic code; select between codes 2 and 5 depending on your species. Finally, in the "ORF start codon to use", choose " 'ATG' and alternative initiation codons". If you had identified gaps in the previous step, you can specify where the program should search ("From" and "To"). Submit the job.

If ORFfinder did find ORFs, you should see a lot of information. On the top of the results window you have a representation of the mitochondria (or of the region you specified) with the predicted ORFs. Have a look at them. How do their length vary? Do they all have the same orientation? (look at the white arrows on the red background) 

Below on the right, you have a summary of the different ORFs. If you highlight one of the ORFs, its sequence (in amino acids) will be shown in the window on the left. Finally, below that left window, you can click on "SmartBLAST". This option can very quickly identify proteins in the ORFs. This is very useful and can help you decide whether an ORF is really a gene or not (if an ORF has no good hit, it suggests that maybe there is not really a gene there).

**From now on, the instructions will differ whether you looked at a certain region of the mitochondria or if you looked at the entire mitochondria.**

### If you looked at smaller regions:

Did ORFinder find anything? If it didn't, in any of the regions, run it again for the entire mitochondria and proceed to "If you looked at the entire mitochondria".

If ORFfinder did find something, run SmartBLAST on the ORF(s). If the ORF has good hits, this suggest that there is really something in the gap. It is possible that ORFfinder identified several ORFs belonging to the same gene. You can add the new gene to your GeSeq output file. Copy the lines corresponding to an existing gene (both the "gene" and the "CDS" information) and paste it in the right location. Then modify the start and end of the gene, its name and, if you want, add the amino acids sequence. Repeat if you looked at more gaps. Finally, run OGDraw (see Step 5) on your modified GeSeq file. Save the output as you will need to submit it.

**Question 7 (alternative 1). What are the new genes identified by ORFfinder?**

### If you looked at the entire mitochondria

Choose three of the ORFs and perform SmartBLAST on them. Answer the question below for these three ORFs.

**Question 7 (alternative 2). What are the genes identified by ORFfinder? Do the results match with your previous results, e.g. from GeSeq? (e.g. in terms of boundaries)**

### Step 7: A bit of programming

**Question 8. Write a Python script which takes as input a whole mitochondria fasta file and the coordinates of a feature (start and end) and outputs a fasta file with a informative header (including: the species name and / or identifier, the name of the feature, and the coordinates of the feature) and the sequence of the feature (i.e. the sequence between the start and the end positions).**


You can use either parsing through the command line thorugh `argparse` or `sys.argv` from the `sys` library [example here](https://www.pythonforbeginners.com/system/python-sys-argv), or interactively using `input()`.
An example of the first method below

`my_script.py input_mitocondria.fasta Gene_name start stop Extra annotation`

```
my_script.py input_mitocondria.fasta TGH_4 5001 5100 This is a cool gene

## Output:
cat gene_1.fasta

>TGH_4:5001-5100 This is a cool gene
ATGACATATGCTTTGTTTCTGTTGAGTGTAATTTTAGTGATAGGGTTCGTGGGGTTTTCTTCTAAGCCCT

```


---

## Report:

Please submit a text file with answers to Questions 1 through 7.

Submit the visual representation of your annotated mitochondria.

Submit the script from Question 8 as a .py file.

---

This is the end of the lab, please make sure that you completed and wrote down the answers to all of the questions.
Upload the **scripts** (code) that you were asked to submit to studium **in the original format** (i.e. .py or .sh), no `pdf` or word files! Any answers that are not code should of course be in text formats such as `.pdf, .txt & .docx`.
Also, make sure to delete any files that you no longer need - you can copy them somewhere else if you want to keep them. This goes for both the Unix computers and Uppmax.
