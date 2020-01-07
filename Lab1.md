# Lab 1 - basic command line tutorial

### What is UNIX?

### Why are Unix systems so popular in science?




#### 
Interaction with UNIX-style systems is typically done through a command-line interface (CLI) - a `terminal` of some sort. There is generally no GUI (graphical user interface), though there exist protocols to display graphics through the terminal such as `X11`.

To communicate with the system there needs something to interpret the user's command. In a UNIX-like system, this is called a `shell`, one of the most common ones - and the one found on `Uppmax` is called Bourn-Again shell or simply `bash`.
It's an interpreter and it's own (basic) programming language. 

Enough exposition, let's get going. Open up the terminal and proceed with the exercise. 

#### Moving around
When you connect to a system you usually end up in your home directory. To see the path to where you stand use the `pwd` command. Try it now:

```
pwd
```
it should return something like:

```
/home/user_name
```
As you move around in the systems directories this will of course change.

To make a directory (called folders on other systems) use the command `mkdir`, try the following out:

```
mkdir directory1
```
To figure out what happened use the `ls` command which lists the content of the current working directory:

```
ls
```
As you can see `mkdir` makes directories, all (or at least most) UNIX commands are named after their function. 

To go to your new directory use `cd` (change directory);

```
cd directory1
```

Now try to create another directory called `directory 2`

```
mkdir directory 2
```
Take a look at what you did with `ls`.

```
ls
2        directory
```
Looks like you created two directories, one called `2` and another called `directory`. Since the basic syntax for UNIX commands is:

```
command option1 option2 option3
```
Each extra option to the command is separated by a space, which means that spaces and other white characters, such as tabs, are not allowed in file or directory names!

To fix this issue use `rm` for, you guessed it remove.
We can remove both at the same time:

```
rm directory 2
```
Ouch, `rm` by default only removes files, not directories. You need to tell `rm` that you want it to work recursively, using what's typically called a flag, in this case `-r`.

```
rm -r directory 2
```
Check that is worked using `ls`.


Ok, let's try and make a second directory again:

```
mkdir directory2
```
change into it using `cd` 

```
cd directory2
```

So now your current directory should be `home/your_usename/directory1/dirextory2`, to find out use `pwd`. If you want to go one directory up, in our case from directory2 to directory1 you can use `..` notation:

```
cd ..
```

Check that it took you to the right place. Here are two need things to know about `cd`

```
cd -
```
takes you back to the last place you were standing.
Just `cd` with no options takes you to your home directory.






### Playing around with files

```
w3m -dump https://en.wikipedia.org/wiki/Principal_component_analysis > PCA.txt
```


The above command reads the Wikipedia page for Principal Component Analysis and extracts the body text and saves it to the file `PCA.txt`. The `>` is used to redirect output to a file.


Now that we have some text to work here are some tools for inspecting files, try them out on `PCA.txt`.

```
cat - concatenates the file contents to standard out (the screen)
less - a nice and easy file viewer, press q to quit!
head - look at the head of a file, by default the first 10 lines.
tail - looks at the tail of a file, by default the 10 last lines.
```

It turns out that the PCA article is quite big, how big?
Counting is something that is hard and slow for humans, but incredibly easy for machines. Use the word count command `wc` on the file to figure out how many lines and words it contains. 

What did you get? How many lines and words?

Hmm, it's not that clear, is it? Have a look at the manual for `wc` to try and figure it out. 
All core UNIX commands have an inbuilt manual you can access it through the `man` command:

```
man wc 
```

Now that you figured that out, use the manual for `head` to figure out how to save the first 100 lines of `PCA.txt` and save them into `short_pca.txt`.

You can use `wc` to figure out if you did it correctly.

#### grep
`grep` is a useful tool that prints lines matching a provided pattern.
In our example we can use it to figure out how many lines contain the word `PCA`:

```
grep PCA short_pca.txt
``` 


### Pipes and multiple commands
One of the fundamental concepts behind UNIX from the beginning was an emphasis on small task-specific programs. These programs could then be chained together into pipelines to perform more complex tasks.

Imagine that you have a machine that cuts down trees, de-barks them and cuts them into planks. If you have trees and wants planks then this is fine, but what happens if you want to cut down the tree and keep the whole log? Your big fancy machine only makes planks.
In the UNIX world, your one machine would consist of smaller machines chained together. One that cuts down the tree, one that removed the bark and one that cuts into planks. 
If you get a pile of logs from your neighbor then you can use one of your machines to make planks, etc.

This type of chaining together is called piping in UNIX and is done by the pipe character `|`. E.g.

```
command 1 | command 2 | command3 > output_file
```

By using `grep`, `pipe`, and `wc` we can now easily figure out how many lines of the Wikipedia article about Principle Component Analysis that contains the word `PCA`:

```
grep PCA short_pca.txt | wc -l
```

Try it for the full article as well!
Write down the answers!

--

### Hidden word exercise 
Now that you have some basic UNIX tools at your disposal go and do the [hidden word_exercise](hidden_word_exercise_instructions.md).

Do not continue with the next part until you are down with it. 

--

#### Working remotely 
The next part of this exercise will take place on the computational cluster Rackham on UPPMAX (Uppsala Multidisciplinary Center for Advanced Computational Science). 
To connect to a remote Unix server the protocol `ssh` is typically used.

Given that you have an account with Uppmax do the following to connect to Rackham:

```
ssh your_user_name@rackham.uppmax.uu.se
```

After entering that you command you will be prompted to enter your password.





Ok time for something perhaps a bit more fun. Some genetic data!


#### Manipulate blastoutput? 

### BAM files

In directory XX/XX you have a `.bam` file. The SAM/BAM (Sequence Alignment/Map & Binary Alignment Map) format is a very popular format for storing nucleotide data that is aligned to a reference. 
If you want to read more about the file format(s) you can have a look at the official documentation:
 https://samtools.github.io/hts-specs/SAMv1.pdf

If you want a simpler (and easier to read) text to give you an overview have a look at the Wikipedia article: 
https://en.wikipedia.org/wiki/SAM_(file_format)

The main tool for working with SAM/BAM files is called `samtools` and it's installed through the module system on Uppmax. To get access to it:

```
module load bioinfo-tools
module load samtools/1.9
```

Before using it have a look at the file sizes of the two different formats.

```
ls -lh 
```

With that information, you can probably see why it's a generally good idea to store data in binary formats as much as possible. The original full file is 117 GB.

##### The `.bam` file is just for a small part of the genome, which ones? 
use `samtools view` and `head` and `tail` to figure out the first and last position.
 

##### Use `cut` to extract only the name and nucleotide sequence from the `.bam` file. 

First, figure out which fields it is that you want and then investigate `man cut` to figure out how to access them.


#### More uppmax stuff
Possible things:

```
 - modules 
 - uquota
 - jobinfo
 - interactive window
 - x11 evince etc.
 - slurm, submitting jobs. 
```

 file/directory architecture?
 Lab1 , Lab2
 bash loop?
 
 
 toy examples of a bash script?


