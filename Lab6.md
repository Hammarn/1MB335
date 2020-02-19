# Session 6 - project
For the following labs you will work on a evolutionary biology project were you will try to answer one of the questions below using phylogenetic methods. You will be randomly assigned one of the questions. You will need to gather your own dataset for the analysis. We (the lab assistans) will help and guide you so that you end up with a suitable dataset, but ultimately the choise of samples is yours. 

## Questions:
1. Are bats more closely related to horses than to cows?
  
2. Do marsupials form a monophyletic group (i.e. clade)?

3. Both whales and dugongs originate from landliving animals. Did this land-to-water transition occur twice independently?

4. Are salamanders more closely related to frogs than to lizards?

5. What are the closest relatives of octopuses and squids?

6. Is the guinea pig more closely related to rats than to pigs?

7. What feline (cat-like animals) is most closely related to the cheetah?

8. Are egg-laying mammals (platypus and echidna) more closely related to marsupials than to placental mammals?


### Pointers

When chosing your species you need to think about what species you want to test/compare i.e. your ingroup as well as your outgroup: 

![](Outgroup.jpg)
_By Ngilbert202 - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=63950569_

The test in the above figure would have been to see if `C` is more related to `B` or to `D`, and the answer would then be that `C` is closer to`D`. 

* 3 You will of course have to have some whales and dugongs but also several different clades of landliving mamals to determine the potential closest relatives.

* 5  In order to be able to answer this question you will need to have species from _several_ different distinct lineages as well as a few squids/octopuses. 



You will start with compiling your datasets in this lab. The following labs, 7 till 8, will introduce different phylogenetic methods, programs and tools that you will apply to the dataset you compiled. You will have to submit a few items along the way.


**N.B.** Since you are going to produce quite a lot of files, try to use self-explanatory files names and a good structure of folders. It will make your work easier. It might be a good idea to write a short description about how the archive is organized and where the files are (trees, scripts, alignments and so forth)


### Gathering your data



First start by actually selecting what species you should use. Think about what ingoups you need to answer the question and what could be a good outgroup. 
If you have a hard time coming up with good candidate species you can use the [taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Root).


You should have around 15 species (15-20) in you dataset. 


**Question1**: write down a few sentences on the selection of species and outgroup in your dataset. Which species did you go with an why?
This will help you later to reflect upon the question and your results.


## Getting the sequences
This should be familiar to you, since you have had to find and dowload sequences before.
Your taks is to gather the full mitochondrial genomic sequences for your species as well as the gene ` CytB ` (Cytochrome b). You should thus have two fasta files per species! 

#### Method A - prefered
* Go to the [NCBI browser for organell genomes](https://www.ncbi.nlm.nih.gov/genome/browse#!/organelles/). 

* On the top right click filter and select `mitochondrion`. * 
* Then search for your species. For the cytB part you need to make sure that you select a mitochodria that is annotated (scroll down and see if there are genes and coding sequences listed).

* Click and dowload the fasta file for the entry as you have done several times before. 


#### Method B - if A doesn't get you what you want

* Use BLAST to find sequences that are not in the curated "nice" list of organells. 

* Start with one of the species for which you have the sequence. 

* BLAST that sequence to find related sequences 

OBS! Before choosing a sequence have a look at its length - the hits should not be much shorter than the query. Additionally, as a sanity check, you should see that all of your sequences have a relative similar position on the mitochondrial genome (except possibly your outgroup sequences).


Save your files with smart, distinguishable names.

## Create a name conversion file.

Create a tab-delimited file with three columns. The file should contain one row for each sequence in your data set, including: 

 * a maximum 8-character short-name (enough for you to identify it: e.g. c_Vurs)
 * an easy-readable name (good for presentation to others: e.g. cytB_Vombat_ursinus)
 * a globally unique identifier (e.g. NC_026542.1:14178-15317).


**Question 3** Now you should write a python script that takes a fasta file as input as well as your conversion table and then can switch between the three different header types.

Submit the script and the conversion file!
