# Session 3 - Prepare your mitochondrial genome

## General introduction to sessions 3 to 5

<!-- Complete and improve! -->
In these three labs, you will work with mitochondrial genomes. Mitochondria are present in all eukaryotic cells (for a review, see 'Origin and diversification of mitochondria', Roger et al.), where among many other functions it supplies the cells with chemical energy (ATP). Here, we will focus on the genomes present in mitochondria; mitochondrial genomes present the advantage of being relatively small compared to nuclear genomes (e.g. 16,000 base pairs in humans), thus facilitating bioinformatic operations in the labs. They are also present in many copies in the cells, thus they are relatively easy to sequence even in extreme cases where DNA is often limited such as environmental DNA or ancient DNA studies. Although mitochondrial genomes can take many different forms depending on the species, they all contain a series of conserved protein-coding genes as well as rRNA and tRNA; this makes mitochondrial genomes good candidates for comparative analyses between different species.

During these three sessions, your main task will be to annotate the mitochondrial genome of one of the following organisms: great apes, mouse, fruit fly or nematode. When you each have annotated the genome of your organism, you will compare and contrast your annotations with those from other students who worked on the other species. To complete this task, you will need what you learned during sessions 1 and 2, and you will use some parts of your annotated mitochondrial genome and that of your colleagues during sessions 6 to 8.

The steps you will follow in sessions 3 (assembling the genome) and 4 (annotation) are similar to what you would do if you were to annotate *de novo* an unknown mitochondrial genome. However, as the goal of these labs is mainly to familiarize yourself with bioinformatics rather than with annotation, we chose to work with model organisms (or close relatives of model organisms) for which annotated genomes are already available. This means that your task will be greatly simplified. However, you should be able to use the same tools to annotate a new mitochondrial genome if you wish too!

## Introduction / Background information to session 3

You received a whole-genome assembly comprising nuclear and mitochondrial contigs of various sizes. Before you can start the annotation, you will need to reconstruct the mitochondrial genome, by identifying mitochondrial contigs and placing them in the right order so that they form a circular genome (we will work only with species with a circular mitochondrial genome). To do that, you will use different types of BLAST as well as a very useful command, `grep`. Moreover, you will need additional resources, which are described in the 'input' section. Once you have a circular genome, you will need to localize the canonical start (to orient the genome). After all of this is done, you will be all set for starting annotating in session 4!

## Goals

  + Prepare a circular, orientated mitochondrial genome for annotation.
  + Get familiar with the NCBI webpage and some of its content (tools, databases etc).

## Input(s)

  + an assembly (format: `fasta`) for your species of interest. This assembly consists of contigs which need to be assembled (in your case you are only interested in the mitochondria, so you will need to identify the mitochondrial contigs).
  + a set of proteins from a close relative of your species of interest. This will be used to identify the contigs belonging to the mitochondria in the assembly.
  + a library of short reads (format: `fastq`) for an individual for your species of interest. This will be used to bridge the mitochondrial contigs.
  <!--I choose to work with the coding sequences not the gene features for the protein set-->

## Output(s)

<!-- what do we consider to be an output? for example, is the blast output one? or only the circularized mitochondria?-->

  + a circularized, orientated mitochondria for your species of interest (format: `fasta`).
  
## Tools

  + command line blast
  + web-based blast
  + NCBI
  
## Steps

  + `blastx`: blast the assembly to the set of mitochondrial proteins to identify the mitochondrial contigs,
  + validate via web-based blast that the identified contigs are mitochondrial,
  + create a new fasta file with mitochondrial contigs,
  + tile,
  + orient to the canonical start location in the mitochondrial genome (cox1).

## Details

### Set up your working space

If you have not done so before, now is a good time to set up your working space on the cluster.

The course is accessible at: `/proj/g2019029/private/`

You will find data in: `/proj/g2019029/private/DATA/` and scripts in `/proj/g2019029/private/SCRIPTS`.

Create your own folder under: `/proj/g2019029/private/RESULTS` (for example: `firstname_lastname`). Think about how you want to organize this folder. For example you might want a folder for each tutorial; you might also want to reproduce the DATA / SCRIPTS / RESULTS structure; etc.

### Identify the mitochondrial contigs in your assembly    

For this step you need two inputs: the assembly (.fna) and a set of proteins from a species related to your species of interest. The assembly contains many contigs from both mitochondrial and nuclear DNA. You need to identify the mitochondrial contig(s). For this you will use command-line BLAST between your assembly and a set of mitochondrial proteins from a related species. BLAST comes in different flavors, and thus it matters whether the sequences are coded as nucleotides or as amino acids.

The assemblies are in subfolders of: `/proj/g2019029/private/DATA/assemblies`

The set of proteins are in: `/proj/g2019029/private/DATA/coding_sequences`

**Question** Are the sequences for the assembly and the set of proteins in nucleotides or in amino acids? What is the format of these files?

Comment: the assembly file is compressed; use for example `zcat` to visualize it.
<!-- nucleotides for the assembly. For the set of proteins so far I have used nucleotides too. Fasta. -->

Before running BLAST, you need to make a database out of the set of proteins. On Uppmax you will first have to start an interactive window (refer to instructions in sessions 1 and 2) and load the corresponding module:

```
module load bioinfo-tools blast/2.9.0+
```

You are going to modify file so you should make a copy to your own folder (of the set of proteins) and work on that copy. Then, adapt and run the following command:

```
makeblastdb -in path_to_the_protein_set/protein_set.fasta -dbtype nucl 
```

<!-- the dbtype could also be prot -->

**Question** How many new files are created? Can you read them? <!-- three files: `.nhr`, `.nin`, `.nsq` All binary `.nhr` is the header, `.nin` the index and `.nsq` is  the sequence file, see here: https://www.biostars.org/p/111501/ . -->

Now we are going to blast. We are going to use `tblastx`, but you can also try other types of `blast` and see what happens. <!--Or we have them try different blast and compare results - e.g. `blastn` can be done with the same inputs. --> Adapt and run the following command, which might take a few minutes to complete:

```
gzip -dc path_to_the_assembly/assembly.fna.gz | tblastx -query - -db path_to_the_protein_set/protein_set.fasta -outfmt 6 -out outfile_name.blast
```

Comment: the first part of the command (`gzip -dc`) is because we need to decompress the assembly file before running blast.

**Question** Open the output file. What do you see? Can you make sense of the different columns? <!-- col1: query contig; col2: match in the database; etc. See here for example: http://www.metagenomics.wiki/tools/blast/blastn-output-format-6 -->

We are interested in column 11, as the best hits will have a low e-value. Adapt and run the following command; can you describe what it does? Adapt the threshold and see what happens.

```
awk '$11 < 0.0001 {print}'  < outfile_name.blast |wc -l
```

Now you have to identify which contigs have many regions with good hits. To do this you run the following command (think about the previous command output to define the e-value threshold - you might need a higher or a smaller value). You can also come up with different strategies if you like.

```
awk '$11 < 0.0001 {print}'  < outfile_name.blast |cut -f1 | sort | uniq -c
```

**Question** Write down the names of the contigs which came up.

<!--Possible question: why do we blast against proteins? Answer: better similarity in the protein domain, particularly relevant for distantly related species. 
Different BLAST:
-tblastx: translated nucleotide database against translated nucleotide query
-blastn: nucleotide-to-nucleotide blast
-blastx: protein subjects using a translated nucleotide query
-tblastn: translated nucleotide database using a protein query
-->

### Validate via web-based blast that the identified contigs are mitochondrial

<!--Is that the step where we also have added a mitochondrial contig from a distant relative and they should notice that?-->

Now you have to validate that these contigs really belong to the mitochondria. You will use online blast and submit a fragment of the configs that you identified at the previous step. To select the fragments, use the bash command `grep` to find the contig in the assembly file. You will need the `-A` tag as well. <!--Do they already know about grep? Also, for this step it might be easier to have one-lined fasta.--> Select a good chunk of the contig.

Caution! Check whether your assembly file is an interleaved (i.e. the sequence is on multiple lines) or a sequential (i.e. the sequence is on a single line) fasta file. If it is interleaved, you need to convert it to a sequential fasta before using the `grep` command above. Normally you should have a python script from Sessions 1 and 2 that does just that. You will use the sequential fasta in the next step too. 

We will take a little detour as it is the first time that you work with NCBI in this course. <!--Possibly this should go somewhere else... At the beginning?--> You will find NCBI main page here: 
https://www.ncbi.nlm.nih.gov 
This webpage provides a lot of resources, databases, programs etc. It is easy to get lost... So before you start working with it you will perform a few tasks to get familiar with it and get an idea of what it can offer you.

**Question** First, click on 'Analyze' in the middle of the page. Check the available tools and make a list of the tools that you think will be useful for this course.

**Question** Go back to the main page. Left of the search field, you have a drop-down menu listing the different databases. Again, which ones do you think will be relevant to us? And where did the input files you received in this lab come from? <!--Assembly, SRA, genomes.--> If you want to see the starting page for a given database, select it in the menu and click 'Search'.

**Question** Go back to the main page if you left it and find the BLAST page, then choose nucleotide blast.

Paste the chunk of sequence that you selected with the grep command above into the dialog box. Below the BLAST button, select 'Show results in a new window'. All other parameters can be kept as default. Perform the blast.

**Question** Does the fragment belong to a mitochondria? Does it belong to the species you are interested in?

Repeat this which each of the contigs that you identified at the previous step. Keep track of the contigs which do belong to the mitochondria of your species of interest.

### Create a new fasta file with mitochondrial contigs

You have identified one or several contigs (usually one to four) belonging to the mitochondrial genome of your species of interest. The next step is to get a continuous DNA sequence. This will be done in this and the next step. Even if you have already a single contig at this stage, please go through the steps! In this step, you will prepare a fasta file that will allow you to perform the next step - 'tiling'.

First, create a fasta file for each of the mitochondrial contigs. The fasta file should include a header and the sequence. Adapt and modify the following command: <!--How often should we stress that they have to think about how they name the output files? and pay attention to the file structure? Should we add questions suggesting to do it in a way or another?--> 

```
grep -A1 name_of_contig path_to_the_assembly/assembly.fna > path_to_output/contig.fna
```

Second, create a single fasta file with the different contigs fasta files. You can, for example, use the command 'cat'. <!-- cat contig1 contig2 > allcontigs.fna--> If you have a single contig, try to create a file with several copies of that contig (do not use it for the next steps though, it is only for training!).

### Tiling

You now need to connect the different contigs in your file to create a continuous circular sequence. This is the step called 'tiling'. Your contigs may come from different strands (+ or -). You won't be able to connect a contig from the + strand to a contig from the - strand. Thus the first step of the tiling is to obtain the reverse-complement for each of your contigs. You can do that by visiting this webpage: https://www.bioinformatics.org/sms/rev_comp.html <!--Or that could be one of the scripts they write?--> Paste your contig sequence into the search box and reverse-complement it. Now add that new sequence to your fasta file (do not forget to add an informative header!). Repeat for each of your contigs.

You are ready to connect the different contigs! For that, you will use another resource: short reads data from an individual of your species of interest. Indeed, there may be gaps between the contigs that you have now. To get a continuous molecule, you need to fill these gaps. This is schematized in Figure X.

![](Figure_Tiling_Pogodaetal.png)

.center[Figure X: An illustration of tiling. Let’s say you have three assembled contigs that you have identified as mitochondrial: Node 12, Node 26, and Node 83 (black lines). You will use reads from the .fastq file (purple lines) to bridge the gap between these three contigs. The blue lines are the sequence that you identified and used to attach the respective contigs to each other for a complete, but not yet circularized mitochondrial genome. Taken from Pogoda et al. A guide to organellar genome assembly and annotation.]

Your task now is to select a library of short reads for an individual of your species of interest. A good place to find that is NCBI. So, open the start page of NCBI again. In the 'All Databases' drop-down menu, choose 'SRA'. 'SRA' is short for Sequence Read Archive.

**Question** Search for your species of interest. How many results do you get?

Most likely your first search resulted in a lot of results. This is expected as you work with model organisms! On the left side of the result page, you have different categories of data and information about the number of results in each of these categories.

**Question** Narrow down the search by selecting some of the categories of data. Think about what you learned about the different sequencing technologies. How many results do you get once you narrowed the search? You can test different combinations of criteria. For those working with human data, make sure to choose 'Public' in the 'Access' field. <!-- Should we give the 'answer'? or guide more the choice? or ask them to justify the choice? In the end it won't matter too much because I am not sure that we will really do the tiling. But it is a good way to get an idea of what is available I find. For example, I think that Source: DNA, Type: genome, Library layout: single, Platform: Illumina, File Type: `fastq` makes sense. But for D melanogaster this combination gives few results...-->

Now that you narrowed down your search, open a few of the results and read the information that is provided. For example, what is the size of the file? When was it published? What do you know about the particular sequencing strategy that was used to generate the data?

<!--Maybe it would be easier to have them, in the end, use an archive that we selected. There is a lot of not straight-forward results... Moreover if we work on Uppmax, it will be easier in terms of space management. It could also be a moment where the students discuss because the different organisms give different results.-->

As you might have noticed, there is a bit of everything in the results. To make it easier for you, we already selected a library of short reads for your species. <!--It would be good to have them use fastq-dump though... Maybe we can do that at another point.--> You will find it in a subfolder of: `/proj/g2019029/private/DATA/sra/`.

**Question** What is the format of the file? Do you understand what the different lines are? How long are the reads? <!--FASTQ - header - starts with @, raw sequence letter, optional header - starts with +, quality value for each of the bases in line 2. For the length of the reads they can use $wc -m.-->  

You are now ready to perform tiling. For that, you will select a short section of nucleotides from the end of your first contig (around 30 bp) and then use grep to find that short sequence in the short reads library. Adapt and run the following command:

```
grep AATTTGGGTTTACTAG path_to_short_reads_library/library.fastq
```

You should see in the terminal a series of reads which contain exactly that sequence. If everything went right, the sequence just after your short sequence (which should be highlighted in the results) is the continuation of your contig. See whether it seems to be the same sequence in all or most of the selected reads. If it is the case, choose one hit where the search 'word' is towards the beginning (caution! invert if you choose a word at the beginning, not at the end of the contig) and select the sequence that comes after the highlighted word. Copy that sequence into your fasta file below the entry of the contig that you selected the word from. Don't forget to add a header!

Repeat this twice - but this time the 'word' in the grep command is from the end of the sequence you just added.

<!--This part can be adapted depending on the data we choose to work with. But it's still might be worth it that they try - if we limit it, e.g. to nine trials and then they are "allowed" to move on.--> 

You should now have three new, short fragments after the contigs in your fasta file. It is time to check whether the newest sequence connects to one of your contigs. Select about 30 base pairs at the end of the newest sequence and search for it within your fasta file. If you are lucky, it will connect to one of your contigs. Reorganize your fasta file so that it goes: first contig; new sequences 1 to 3; contig which connects to the new sequence. Remove the overlap if there are some. Now you can continue with the end of the second contig.

If it does not connect, you have to continue a bit. Take about 30 bp from the end of the last sequence you added, and grep for it in the short reads library. Add the new piece of sequence, repeat two more times. Then grep in your fasta file. Does it connect? If yes, proceed as the previous paragraph. If not, repeat the process in this paragraph one last time. If it still does not connect, have a closer look at your data. Do you see many repeats?

If you have a single contig from the beginning, follow the instructions nevertheless. Does the beginning and end of your contig connect or do you need to add sequences from the short reads?

At this stage, make a copy of your fasta file to keep a record of what you did. Then clean up your fasta file, i.e. remove the headers and sequences of the fragments that you are not using (e.g. the reverse complements of contigs) and make a single sequence of all the contigs and extra bits which belong together (see Figure X - you only want the black and the blue segments). Alternatively, use the ready fasta file here: `/proj/g2019029/private/DATA/mitochondrial_genomes`.

<!--Do we want to include the part about error correction, which involves mapping and visualization? I have not tried to run it yet, but if it works properly it should be interesting for the students.-->

### Orient to the canonical start location in the mitochondrial genome (*cox1*).

Congratulations! You now have a circular mitochondrial genome. The last step today is to orient it to the canonical start location. By convention, non-model organisms' mitochondria are oriented with the *cox1* gene as the first gene of the genome. <!--Does that not apply to model organisms?--> To do that, you will do a pairwise alignment. But first, you have to find a sequence to compare your mitochondrial sequence too. Open an NCBI blast window and select nucleotide blast. Paste your mitochondrial sequence.

**Question** To which organism does the best hits belong too?

Since you are working with well studied organisms, most likely the first hit will align perfectly to the mitochondrial genome of your species. To make it a bit more interesting, we are from now on going to use as a 'reference' a close relative of your species instead of your species itself. You are going to recover the appropriate sequence from NCBI. Use the table below to see which species you should be looking for depending on your start species.

Study organism | Close relative (Model organism)
---------------|---------------
Caenorhabditis remanei | Caenorhabditis elegans
? | Mus musculus
? | Drosophila melanogaster
Chimp? | Homo sapiens

Go to your new favorite webpage (i.e. NCBI ;) ). We will detail one way to find the mitochondrial genome of the close relative. There are more ways, feel free to explore!

In 'All Databases' choose 'Genome' and then under 'Custom resources' choose 'Organelles'. On the new start page, under 'Using organelles resources', choose 'Browse by organism'. Write the name of the species in the search bar. 

**Question** What is the size of the mitochondrial genome? What is the identifier of the sequence? (there might be several identifiers) <!--Info should be easy to find in the table. Give NC number, sometimes also e.g. KY.-->

Then click on the identifier. You should be taken to a page that looks like that one: https://www.ncbi.nlm.nih.gov/nuccore/NC_002008.4, except for your species of interest. If that is not the case, try again or ask the teaching assistants. This page comprises a lot of information, including annotations. You want the sequence of the *cox 1* gene. Search for it on the page (you might have to change case, e.g. COX1). You should get two matches, one for the gene and one for the coding sequence (CDS). Click on the CDS link and open it in a new window. You should have something similar to the entire mitochondria but very reduced in length. To download the fasta file, click on 'FASTA' (under the name of the sequence). Once the page changed, click on 'Send to' in the top right of the page, make sure to choose 'Complete Record', and select 'File' as file destination. The format should be FASTA. This will open a text file with the sequence - save it in an appropriate location with an appropriate name.

Comment about NCBI: as you might start to notice, you can access a given page of NCBI (e.g. the page of the mitochondrial genome) in several different ways, using different identifiers etc.

**Question** Estimate the length of the **cox 1** coding sequence with the command `wc -m`. Does it match with the information in the fasta header? <!--I did it - for C remanei it is not exactly the same... Weird. 15 bp difference.-->

**The next step is described in great detail in the manual from C Pogoda, p14 to 16. I will modify and summarize it here later. The process should not take too long for the students.**

<!--At the moment and considering the part missing above, Lab 3 is about 3000 words long.-->
  
## Report:

<!--make a cartoon of different blast? Submit answers to two or three of the questions?-->

TO DECIDE.

