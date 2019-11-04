# Lab 1 - basic command line tutorial

### What is unix?

### Why are Unix systems so popular in science?




#### 
Interaction with unix-style systems is typically done through a command line interface (CLI) - a `terminal` of some sorts. There is generallt no GUI (graphical user interface), though there exists protocols to display graphics through the terminal such as `X11`.

To communicate with the system there needs something to interpret the users command. In unix-like system this is called a `shell`, one of the most common ones - and the one found on `Uppmax` is called Bourn-Again shell or simply `bash`.
It's an interpreter and it's own (basic) programming language. 

Enough exposition, let's get going. Open up the terminal and proceed with the expercise. 

#### Moving around
When you connect to a system you usally end up in your home directory. To see the path to where you stand use the `pwd` command. Try it now:

```
pwd

```
it should return something like:

```
/home/user_name
```
As you move around in the systems directories this will of course change.

to make a directory (called folders on other systems) use the command `mkdir`, try the following out:

```
mkdir directory1
```
to figure out what happend use the `ls` command which lists the content of the current working directory:

```
ls
```
As you can see `mkdir` makes directories, all (or atleast most) unix commands have names after their function. 

To go to your new directory use `cd` (change directory);

```
cd directory1
```

Now try create another directory called `directory 2`

```
mkdir directory 2
```
Take a look at what you did with `ls`.

```
ls
2		directory
```
Looks like you created two directories, one called `2` and another called `directory`. Since the basic syntax for unix commands is:

```
command option1 option2 option3
```
Each extra option to the command is separated by a space, that means that spaces and other white characters, such as tabs, are not allowed in file or directory names!

To fix this issue use `rm` for, you guessed it remove.
We can remove both at the same time:

```
rm directory 2
```
Ouch, `rm` by default only removes files not directories. You need to tell `rm` that you want it to work recursively, using what's typically called a flag, in this case `-r`.

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








