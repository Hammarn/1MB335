# Session 4 - annotate your mitochondrial genome

## Introduction / Background information to Session 4

<!--How much we write here depends on how much they learn about annotation during the lectures.-->
  
During Session 3, you assembled a circular, orientated mitochondrial genome - basically a sequence of nucleotides. In this session you will make sense of these nucleotides. The mitochondrial genome, like the nuclear genome, codes for proteins, transfer RNA (tRNA) and ribosomal RNA (rRNA). These elements are necessary for the function of the mitochondria. For example, the proteins are involved in ATP synthesis and protein synthesis; the tRNA are necessary for the translation from RNA to protein; and the rRNA are necessary to assemble the ribosomes. Other elements also necessary to the mitochondria' function are coded for in the nucleus.

'Annotation' means finding the location of the different elements in the genomes. This can be done in different ways. For example, one can look for conserved sequences between different species. It is also possible to predict the location of protein coding gene by searching for start codon and promoters. <!--Add more background if needed.--> Once you have annotated the genome and know where a given gene is, it is easy to extract that gene and e.g. use it for comparative approaches (Session 5) or to build phylogenies (like you will do in the bioinformatics project: Sessions 6-8).

Because you are working with model organisms - or close relatives of modern organisms - it will be quite easy to annotate the mitochondrial genome. However, you could follow the same steps if you were working with non-model organisms.

The text from this session is modified from A guide to organellar genome assembly and annotation, by Cloe Pogoda, Kyle Keepers, and Nolan Kane (A CURE-based approach to teaching genomics using mitochondrial genomes, CS Pogoda et al, CourseSource 2019).

## Goals

+ Annotate a mitochondrial genome.
+ Get familiar with some of the features of the mitochondria.
+ Get familiar with some annotation tools.

## Input(s)

+ the circularized, orientated mitochondria for your species of interest (format: fasta), from Session 3.
+ a list of the features that you should find in the mitochondrial genome.

## Output(s)

+ an annotated mitochondrial genome for your species of interest.
+ a graphical representation of the genome.

<!--How are we going to extract information from the output?? And which format do we want the output in exactly? Not clear to me... Check this tool out: https://chlorobox.mpimp-golm.mpg.de/lola_doc.html (same webpage like GeSeq and OGDraw--> 

## Tools

+ [GeSeq software] (https://chlorobox.mpimp-golm.mpg.de/geseq.html)
+ [tRNAscan software] (http://lowelab.ucsc.edu/tRNAscan-SE/)
+ web-based blast
+ [OGDraw software] (https://chlorobox.mpimp-golm.mpg.de/OGDraw.html)
+ [ORF finder] (https://www.ncbi.nlm.nih.gov/orffinder/)

<!--GeSeq has a long page with alternative softwares: https://chlorobox.mpimp-golm.mpg.de/Alternative-Tools.html For example a recent one with apparently ample documentation on github: https://github.com/linzhi2013/MitoZ Maybe if we need more things to do we could try it (or another) - possibly including download from github etc, as this is very realistic for the students! -->

## Steps

+ First annotation with GeSeq
+ Complete the annotation of tRNAs with tRNAscan
+ Use web-based blast to confirm annotations and locate rRNA
+ Draw a visual representation of your annotated mitochondria and identify unannotated regions
+ Look for open reading frames with ORF finder
+ Conclude

## Details

### First annotation with GeSeq

Open [GeSeq] (https://chlorobox.mpimp-golm.mpg.de/geseq.html) in your browser.
On the left hand side of the page under 'FASTA file(s) to annotate' click 'Upload files', and select the appropriate file (your error-corrected, circularized, reoriented .fasta file). Next, click the appropriate boxes to indicate that this is a circular genome and select the correct sequence source (mitochondrial). We suggest leaving the rest of the options available on the left hand side at their default settings. Next, in the middle section of the page under “BLAT Reference Sequences” click “Add NCBI refseq(s)” which will open a new tab where you can select species that are similar to the one you are annotating (closely related species are the best). Refer to the table in session 3 to know which species to choose *Possibly give more details*. Leave the rest of the options in the middle section unselected. Next, click the button to indicate you have read the disclaimer and hit “Submit”. The program should only take a few minutes to run and will produce several files. We are currently interested in downloading the GenBank file.
Next, open this file in your text editor and take a look at the file produced. At this time, we suggest deleting the notes that GeSeq automatically inserted. Search your document for “note=” and delete the entire line. We also suggest looking for duplicated entries. GeSeq uses multiple references and depending on how the researcher’s annotated their genomes there might be features named rps3 and RPS3, both of which are the same feature but GeSeq treats them as separate. Go ahead and delete any redundant features that are duplicated, as again, this is the easiest stage of the annotation to perform this action. You might notice that you have gene, CDS, exon and intron lines for a given feature (i.e., cox1). Delete any lines that say exon and intron and only save the lines that contain information for gene and CDS. If you were to submit your annotation to NCBI, having all of these duplicated entries would be causing issues.

This is a list of the features that are most likely present in your mitochondrial genome. *TODO add the list!*

**Question 1. How many of the features are found by GeSeq?**

### Complete the annotation of the transfer RNAs (tRNAs) with tRNAscan

To find tRNAs, GeSeq uses the program tRNAscan (Lowe & Eddy 1997). To ensure we have found all of the tRNAs, it is best to double check the lengths and identities of the tRNAs found in GeSeq by using the stand alone tRNAscan program, which has a very easy to use web interface. The program may be found [here] (http://lowelab.ucsc.edu/tRNAscan-SE/). In the proper dialog box upload your sequence, change the dropdown box for 'Sequence source' to the right answer for your species and leave everything else as default. Hit submit. tRNAscan is a bit annoying with formatting and might complain about the header of your fasta file (for example). In that case, copy your original fasta file and simplify the header before resubmitting. You can also paste the sequence in the search box.
After a short while, you will see a list of the tRNAs and their locations in your genome. Compare these results to what GeSeq found and note if anything is missing or locations are divergent. Refer to the table for a list of all the amino acids that should be present in your genome and for any conversion that you need to make (Table 2.1). *Include the table*

**Question 2. How many tRNAs were identified? Were they already identified by GeSeq? Do the coordinates differ between the two softwares? If yes, write the two sets of coordinates down. Which do you think are the correct coordinates?** To answer the last question, you can go to the NCBI page of the annotated genome. You can look for example at the length of the tRNA. You can also try to compare directly the coordinates, but because you are working with an orientated genome that might not correspond.

If tRNAscan identified features that GeSeq did not find, add them to the GeSeq output as follow: For example, let’s say tRNAscan found the tRNA for tyrosine, which GeSeq did not find. We will need to add it in. tRNAscan will use the three-letter code tyr, we see from our translation table that the one letter code is Y *(Table 2.1)*. In addition, we see that the anti-codon for tyr is GTA. Therefore, the correct format for gene name will be “trnY-GUA” (all T’s become U’s because we are dealing with RNA not DNA). Refer back to tRNAscan for the boundaries of this tRNA. In the GenBank formatted text file enter the missing tRNAs using the same format as presented for the tRNAs that GeSeq did find.

### Use blast to fine-tune the boundaries of your features

The boundaries (i.e. start and end) identified by GeSeq for the different features might not be accurate. One way to verify the accuracy of the boundaries is to perform blast. For that, you need to navigate to the GenBank entry of your reference (this is the default format of the NCBI entry, e.g. https://www.ncbi.nlm.nih.gov/nuccore/NC_001328.1 for Caenorhabditis elegans). In the top right of your reference’s GenBank page is a dropdown box titled 'send'. Click on this and select 'coding sequences' in .fasta protein format, this will save onto your computer. This contains the amino acid sequence of all the protein coding features of your reference. We will use these sequences to finalize the boundaries of the protein features that we have imported from GeSeq by BLASTing the reference sequence against your own.

First you will verify the boundaries of *cox2*. Then you will perform the same thing for two more genes of your choice. Here are the instructions for *cox2*: Open the `blastx` page of NCBI and select 'Align two or more sequences'. Within the text file you just downloaded from NCBI, search for the string “cox2” and copy the amino acid sequence for this gene. Return to your blastx window. Now paste your copied *cox2* sequence into the bottom of the two dialog windows. Now either paste in or upload your .fasta sequence into the top dialog window. Note that we chose a file rather than pasting a nucleotide sequence into the window. Also, note that you must choose the correct genetic code, otherwise your results will be inaccurate. This will vary according to the taxon and the locus. Depending on your species, you will choose from: Vertebrate mitochondrial or invertebrate mitochondrial. You can find more information about the different genetic code on this [wikipedia page] (https://en.wikipedia.org/wiki/List_of_genetic_codes) (which suggests the alternative code 14 for nematodes - those of you working with nematodes can go ahead and try!).

Also, choose 'Show results in a new window' - this will allow you to change parameters more easily if you need to. Now, submit the blast. Like you did in session 3 when looking for the start of the mitochondria, go to the 'Dot plot' tab. If you have one solid large line spanning the entire vertical span (or most) of the dot matrix that is an indicator that the gene is complete and in one exon. *Here we could include Figure 3.4 from the tutorial.* Then look at the 'Alignments' tab.

**Question 3. Is the gene complete and in one exon? If not, how does it look like? About the alignment: what is the first amino acid position of the reference ('Sbjct') which align well to your mitochondrial genome?**

If the first amino acid position which aligns well to the reference is not 1, it could be that the start amino acid (usually a methionine) is upstream of the corresponding position in your mitochondrial genome *Should we have the figure to make it easier to understand?*. Have a look at your mitochondrial genome and try to find a start codon (ATG for vertebrates, ATA for invertebrates). Look at the end of the alignment too. Does it correspond to the end position inferred by GeSeq? (there might be a difference due to incorporating or not the stop codon)

Now, choose two more genes from the list of coding sequences that you downloaded for your reference genome and repeat the steps you just performed for *cox2*.

**Question 4. Which two genes did you choose? Do they have one or several exons? Do the boundaries match with the GeSeq boundaries? If not, list the GeSeq and the blast boundaries. Does the alignment start at position 1 of the subject? If not, make an hypothesis concerning the location of the start codon in your own genome.**

### Locate rRNA

**todo write** In the manual they use that to validate the features boundaries. It is a long process, involving pairwise alignement, looking at the dot matrixes and possibly inverting the sequences if needed etc. The other reason they use it is to locate the rRNA - process similar to locating *cox 1*. Apparently there are methods to locate RNA genes (but not specifically rRNA) e.g. http://eddylab.org/infernal/ or http://rfam.xfam.org/, and see this too: http://ensemblgenomes.org/info/data/ncrna. Or NCBI local blast against Rfam. Or RNAmmer http://www.cbs.dtu.dk/services/RNAmmer/ (but from what I can read does not look for mitochondrial rRNA?). Lots of tools here too: https://services.healthtech.dtu.dk/ (including prediction of protein structure)   

### Draw a visual representation of your annotated mitochondria and identify unannotated regions

**todo write** Straight forward, nice output; instructions in the manual are outdated. Once the students have the drawing, identify regions where there is nothing (look at the GeSeq output).

### Look for open reading frames with ORF finder

**todo write** For this step they need to select the right genetic code from 30 different! We could make a short list (e.g. with the ones they need and three extra) and have them choose from it. Summary here: https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi We could also have them compare the results using different genetic code. One of the output pages is a visual summary - they could look at it and guess which features are more likely (e.g. one long ORF more likely than several short ones).

### Conclude

**todo write** E.g. they could compare to the list of features we gave them. Same features in the four genomes, only difference is that C elegans does not have ATP8. So it's not really interesting to fill a comparison table.

<!--Is this the step where they get the list of features?-->    
