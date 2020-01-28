# Session 4 - annotate your mitochondrial genome

## Introduction / Background information to Session 4

<!--How much we write here depends on how much they learn about annotation during the lectures.-->
  
  During Session 3, you assembled a circular, orientated mitochondrial genome - basically a sequence of nucleotides. In this session you will make sense of these nucleotides. The mitochondrial genome, like the nuclear genome, codes for proteins, transfer RNA (tRNA) and ribosomal RNA (rRNA). These elements are necessary for the function of the mitochondria. For example, the proteins are involved in ATP synthesis and protein synthesis; the tRNA are necessary for the translation from RNA to protein; and the rRNA are necessary to assemble the ribosomes. Other elements also necessary to the mitochondria' function are coded for in the nucleus.

'Annotation' means finding the location of the different elements in the genomes. This can be done in different ways. For example, one can look for conserved sequences between different species. It is also possible to predict the location of protein coding gene by searching for start codon and promoters. <!--Add more background if needed.--> Once you have annotated the genome and know where a given gene is, it is easy to extract that gene and e.g. use it for comparative approaches (Session 5) or to build phylogenies (like you will do in the bioinformatics project: Sessions 6-8). <!--Say something that it would be more difficult if they did not have model organisms, and that we are going to cheat a bit?-->

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

+ GeSeq software https://chlorobox.mpimp-golm.mpg.de/geseq.html
+ tRNAscan software http://lowelab.ucsc.edu/tRNAscan-SE/
+ web-based blast
+ OGDraw software https://chlorobox.mpimp-golm.mpg.de/OGDraw.html
+ ORF finder https://www.ncbi.nlm.nih.gov/orffinder/

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

**todo write** - but basically I followed the instructions in the manual. As a reference we should not choose our own species I think (too 'easy' and does not make much sense).    

### Complete the annotation of tRNAs with tRNAscan

**todo write** - but basically I followed the instructions in the manual. The software is a bit picky with format. And it found only three of the 22 tRNA... Possible task: compare the boundaries of tRNA found in GeSeq and in tRNAscan. Which are correct? 

### Use web-based blast to confirm annotations and locate rRNA

**todo write** In the manual they use that to validate the features boundaries. It is a long process, involving pairwise alignement, looking at the dot matrixes and possibly inverting the sequences if needed etc. The other reason they use it is to locate the rRNA - process similar to locating *cox 1*. Apparently there are methods to locate RNA genes (but not specifically rRNA) e.g. http://eddylab.org/infernal/ or http://rfam.xfam.org/, and see this too: http://ensemblgenomes.org/info/data/ncrna. Or NCBI local blast against Rfam. Or RNAmmer http://www.cbs.dtu.dk/services/RNAmmer/ (but from what I can read does not look for mitochondrial rRNA?). Lots of tools here too: https://services.healthtech.dtu.dk/ (including prediction of protein structure)   

### Draw a visual representation of your annotated mitochondria and identify unannotated regions

**todo write** Straight forward, nice output; instructions in the manual are outdated. Once the students have the drawing, identify regions where there is nothing (look at the GeSeq output).

### Look for open reading frames with ORF finder

**todo write** For this step they need to select the right genetic code from 30 different! We could make a short list (e.g. with the ones they need and three extra) and have them choose from it. Summary here: https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi We could also have them compare the results using different genetic code. One of the output pages is a visual summary - they could look at it and guess which features are more likely (e.g. one long ORF more likely than several short ones).

### Conclude

**todo write** E.g. they could compare to the list of features we gave them. Same features in the four genomes, only difference is that C elegans does not have ATP8. So it's not really interesting to fill a comparison table.

<!--Is this the step where they get the list of features?-->    
