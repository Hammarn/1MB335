# Session 1 - basic command line tutorial

### What is UNIX?
Unix is an operating system that was originally developed at Bell labs in the 1970s. It is based around a "modular design" where tools do very distinct and narrrow tasks. To complete more complex tasks multiple modules are then combined through the use of "pipes" - more about those later. 
If you are interested in learing more about UNIX then you can have a look at the [wikipedia article](https://en.wikipedia.org/wiki/Unix) for UNIX, it's quite thorough and well written.  
### Why are Unix systems so popular in science?
While there is no strightforward answer to this question there are some things that are often brought up. UNIX (and unix-like systems) in it's design is quite simple and is nowadays very portable. This has lead to it being used to run anything from massive high perfomance computer clusters to tiny single board computers such as arduinos & raspberry pis. This ubiquity and popularity is probably one reason to why it is still so popular. Since the year 2000 Mac computers are also running on apples own Unix system, another popular unix-like system is the Android mobile operating system. 
While the original UNIX operating system is a comercial system there are many Unix-like operating systems such as Linux which are free and open source (_these are generally based on the Linux kernel_).
The ecosystem of open source and free distribution suits the academic world very well. It is not really research if you aren't charing your findings and how you came to your conclusions - that generally includes your code. 



#### Using UNIX
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
Take a look at what you did using the `ls` command.

Looks like you created two directories, one called `2` and another called `directory`. Since the basic syntax for UNIX commands is:

```
command option1 option2 option3
```
Each extra option to the command is separated by a space, which means that spaces and other white characters, such as tabs, are not allowed in file or directory names!

To fix this issue use `rm` for, you guessed it - remove.
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
Counting is something that is hard and slow for humans, but easy for machines. Use the word count command `wc` on the file to figure out how many lines and words it contains. 

**Question: What did you get? How many lines and words?**

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
**Question:** Write down the answer to the occurrences of the phrase `PCA` in both the full `PCA.txt` and the `short_pca.txt`.

--

### Hidden word exercise 
**Question:**
Now that you have some basic UNIX tools at your disposal go and do the [hidden word_exercise](hidden_word_exercise_instructions.md).

Do not continue with the next part until you are done with it. 
Make sure to report the answer to the question to one of the lab assistants. 
--

### Working remotely 
The next part of this exercise will take place on the computational cluster Rackham on UPPMAX (Uppsala Multidisciplinary Center for Advanced Computational Science). 
To connect to a remote Unix server the protocol `ssh` is typically used.

Given that you have an account with Uppmax do the following to connect to Rackham:

```
ssh your_user_name@rackham.uppmax.uu.se
```

After entering that you command you will be prompted to enter your password.

Our teaching project is called `g2019029`

Navigate to the RESULTS folder (using `cd`):
to:

```
/proj/g2019029/private/RESULTS
```

There you need to make a directory for you to work in. Call it your firstname underscore your last name:

`FirstName_LastName`

For the rest of your exercises you should be working in that directory. I.e copy data there and work on it. 

---


Ok time for something perhaps a bit more fun. Some genetic data!


### BAM files

The SAM/BAM (Sequence Alignment/Map & Binary Alignment Map) format is a very popular format for storing nucleotide data that is aligned to a reference. 

If you want to read more about the file format(s) you can have a look at the official documentation:
https://samtools.github.io/hts-specs/SAMv1.pdf

If you want a simpler (and easier to read) text to give you an overview have a look at the Wikipedia article: 
https://en.wikipedia.org/wiki/SAM_(file_format)

The main tool for working with SAM/BAM files is called `samtools` and it's installed through the module system on Uppmax. To get access to it:

```
module load bioinfo-tools
module load samtools/1.9
```

The **BAM** file and corresponding **SAM** file can be found here:

```
/proj/g2019029/private/DATA/BAM
```

Before using it have a look at the file sizes of the two different formats.

```
ls -lh 
```

With that information, you can probably see why it's a generally good idea to store data in binary formats as much as possible. The original full file was 117 GB for reference.

##### The `.bam` file is just for a small part of the genome, which ones? 
**Question:** use `samtools view` and `head` and `tail` to **figure out the first and last position in the file**. Also include the exact command you used!
 

##### Use `cut` to extract only the name and nucleotide sequence from the `.bam` file. 

First, figure out which fields it is that you want and then investigate `man cut` to figure out how to access them.



### sed and regex
Regular expressions(regex) are used to catch and match certain words or phrases. E.g
^
`^P[0-9]+` will match in the begining of a line(`^`) the letter P literally, any  number (`[0-9]`) repeating (`+`)
it will thus catch the top line but not the second:

```
P674353
454646464 P 
```
These types of expression can be very useful and powerful 


`sed` is a powerful tool for editing streams of files. It is a common way of using rexes in unix. It's often used to replace one thing with another:

if `My_file.txt ` contains:

`dog dog dog`

Then:

```
sed 's/dog/cat/' My_file.txt. # s is for substitute
cat dog dog
```
the first instance of `dog` is replaced with `cat`. We can also replace all instances using the `g` global flag:

```
sed 's/dog/cat/g' My_file.txt. # sg - substitute globally
cat cat cat
```


You can use `sed` on piped output from another program or straight on a single file. For a short summary of some things that you can do with it have a look at [this link](https://github.com/tldr-pages/tldr/blob/master/pages/common/sed.md).



**Question:**
You have been given a that has been exported from excel in an odd format (something that is all to commomn in the life of a bioinformatican). Your task is to transform the file [orange.csv](example_data/orange.csv) into a normally formated `.csv`-file. That is the decimal point should be a `.` and the delimiter (what separates one column from another) should be `,`. It also looks like someone has accidentally inserted some letters among the numbers, they also need to be removed.

Submit what `sed` command(s) you used to clean the file. (Make sure that it looks correct)

_You will probably have to look up more information on how to do this. You can use `man sed` or `info sed` for mor information, or google your way to it. As long as you know what your command does_


### Basic bash scripting for future reference 
Bash is a programming language in itself so it is possible to set up quite advanced workflows with it. The most simple bash script is just a normal command you would type on the command line saved to a file. Or more realistically you might want to run a couple of things that takes a few minutes or hours after each other.
This is something that you definetly will do in your future bioinformatic career.

An example of something like that:

```

echo “Wait for 5 seconds”
sleep 5
echo “Completed”

```

Add the above text to a file called `sleep.sh` and the execute it with

```
bash sleep.sh
```

You can see that the code is executed sequentially, it does not progress to the next line until the previous one has finished.

An example of use case could be that you have data on a local server that you want to transfere to a remote server where you want to perform some kind of analysis and then transfer the results back to your local server. That would look something like this:


```
### Standing at the remote server copy the local files there
scp my_user@remote_server:local_file .
### Do the analysis
run_analysis.sh local_file > output_file
### Copy results back
scp output_file my_user@remote_server:
```


---

This is the end of the lab, please make sure that you did and wrote down the answers to all of the questions.
Also make sure to delete any files that you no longer need - you can copy it somewhere else if you want to keep it. This goes for both the Unix computers and Uppmax.




