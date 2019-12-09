# Lab 2 - Python
In this lab, you will get an introduction to the programming language Python. 
## Introduction 

The Wikipedia article for python has the following to say about it:

```
Python is an interpreted, high-level, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.
Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[27]

Python is dynamically typed and garbage-collected.
It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
Python is often described as a "batteries included" language due to its comprehensive standard library.[28] 

```
https://en.wikipedia.org/wiki/Python\_(programming\_language)


As you might have gathered from the above excerpt, Python as an explicit goal of readability. The use of indentation to denote code blocks forces the programmer to properly indent their code. Take a look at the example below:

```
if True:
   print("True")
else:
   print)"False")
```
as compared to the code below which will result in an error:

```
if True:
print "Answer"
print "True"
else:
print "Answer"
print "False"
```

In many other programming languages (such as Java & C) `;` denotes a linebreak, while it is possible to use it in Python the preferred way of denoting a new line is simply a text line break (i.e hitting enter on your keyboard. )


### Hello world

Now it's time for you to write your first python program. We will start with the iconic "Hello world".
Create a file in which you call the inbuilt print function with the text "Hello World".
Save the below text to a file (hello.py) and call it:

```
print("hello world")
```


```
python hello.py
```


### Datatypes 
There are three types of numeric data in Python:

```
Integer: Positive or negative whole numbers
Float: A fraction of some type, i.e 0.5
Complex number: A number with a real and imaginary component represented as x+yj. x and y are floats and j is -1(square root of -1 called an imaginary number)
```

Integer and float are the only two we need to care about right now.

Open the python interpreter and try the following out:

```
>>> x = 4
>>> y = 5
>>> x+y
9
>>> x/y
0.8
```
We can use the inbuilt `type` function to see what types of data the above things are:

```
>>> type(x)
<class 'int'>
>>> type(x/y)
<class 'float'>
```

The next type of data are booleans, i.e. `True` or `False` (note the capital letters)

Next, we have sequence types:

```
String: A string value is a collection of one or more characters put in single, double or triple quotes. 
List: A list object is an ordered collection of one or more data items, not necessarily of the same type, put in square brackets.
Tuple: A Tuple object is an ordered collection of one or more data items, not necessarily of the same type, put in parentheses.
```

Strings are, as you can see just characters, such as our "Hello world" example above. 

They can be assigned as such:

```
>>>my_string = "Hello"
```
And lists:

```
>>>my_list = ['Hello', 'word']
```

Both lists and strings can be sliced and indexed:

```
>>>my_string[0]
'H'
>>>my_list[0]
'Hello'
```

As you can see Python is 0 indexed. 
You can use `[-1]` to get the last item of a list or string, and `[-2]` to get the second last et cetera.  
It's even possible to access intervals(range)of indexes. This is used with the colon `:`. For instance:

```
my_string[:-1]
```
Returns everything except the last index. 

```
my_string[1:-1]
```
Returns everything except the first and last index. 

Python lists contains many unbuilt methods for interacting with lists. As they are mutable it's possible to add and remove items. Such methods are called on the list with dot notation as such:


|Method | Description|
---|:---|
|.append()|    Adds an element at the end of the list|
|.clear()|    Removes all the elements from the list|
|.copy()|        Returns a copy of the list|
|.count()|    Returns the number of elements with the specified value|
|.extend()|    Add the elements of a list (or any iterable), to the end of the current list|
|.index()|    Returns the index of the first element with the specified value|
|.insert()|    Adds an element at the specified position|
|.pop()|        Removes the element at the specified position|
|.remove()|    Removes the first item with the specified value|
|.reverse()|    Reverses the order of the list|
|.sort()|        Sorts the list|
Used in practise:

```
>>> my_list.append("cool beans")
>>> my_list
['Hello', 'word', 'cool beans']
>>>my_list.pop()
'cool beans'
>>> my_list
```



The main difference between tuples and lists is that lists are mutable, which means that you can add or delete items to a list once it is created. Tuples are unmutable and cannot be changed once created. This fact can be utilized to sometimes improve performance, typically if you are storing the same value as different variables as they will then point to a single memory address instead of one each which would be the case for lists.  


#### Dictionaries
Dictionaries are unordered collections of data in key:value pairs. Curly brackets are used to define dictionaries:

```
thisdict =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
Mustang 
```

It's also possible and useful to create dictionaries with lists in them or lists of lists. Some examples:

```
>>> schedule = {}
>>> schedule['Rickard'] = ['Monday', 'Tuesday', 'Friday']
>>> schedule['Gwenna'] = ['Tuesday', 'Wednesday', 'Thursday','Friday']
>>> schedule['Pedro'] = ['Wednesday', 'Thursday', 'Friday']
>>> schedule
>>> {'Rickard': ['Monday', 'Tuesday', 'Friday'], 'Gwenna': ['Tuesday', 'Wednesday', 'Thursday', 'Friday'], 'Pedro': ['Wednesday', 'Thursday', 'Friday']}
```
If we then want access the items:

```
 schedule['Gwenna']
['Tuesday', 'Wednesday', 'Thursday', 'Friday']
```
Since that is a list we can use methods that works on lists on that expression:

```
schedule['Gwenna'][0]
'Tuesday'
>>> schedule['Gwenna'][-1]
'Friday'
len(schedule['Gwenna'])
4
``` 
`len()` returns the lenght of the provided object (string, list, dict etc.)

Dictionaries have several inbuild methods some of these are:

|Method | Description|
---|---
.keys() | returns a list  all the keys
.items() | returns a list  all the items
.pop() | Removes and returns an element from a dictionary having the given key


### Loops

#### If


#### While 


```
counter = 1
while counter < 5:
    print(counter)
    counter+=1
```




### Formatting Fasta files
The `.fasta` format is the most common format to handle nuclear and/or amino acid sequences. It gets its name from the FASTA sequence alignment software, which is now obsolete but the format lives on. It's a plain text format where the greater-than sign (>) indicates the start of the header and the following line(s) is the sequence. 

Example sequence:

```
>MCHU - Calmodulin - Human, rabbit, bovine, rat, and chicken
ADQLTEEQIAEFKEAFSLFDKDGDGTITTKELGTVMRSLGQNPTEAELQDMINEVDADGNGTID
FPEFLTMMARKMKDTDSEEEIREAFRVFDKDGNGYISAAELRHVMTNLGEKLTDEEVDEMIREA
DIDGDGQVNYEEFVQMMTAK*
```
Your task is to write a python program that takes a file that contains a sequence like the one above where the sequence spans over multiple lines and convert it into a one where the sequence is stored on a single line. 

### Reverse complement
A very common problem that arises when working with sequence files is that sequence information can be encoded on either strand of the DNA molecule. So when the DNA is sequenced it's basically random in which orientation your sequence it. Thus it is important to be able to reverse complement your sequence. 

Task:
Write a program that takes a nucleotide fasta file as input and returns a reverse complemented files as output. 

E.G

```
>NC_011137.1:5899-7440 Homo sapiens neanderthalensis mitochondrion, complete genome
ATGTTCGCCGACCGTTGACTATTCTCTACAAACCACAAAGACATTGGAACACTATACCTACTATTCGGCGCATGAGCTGGAGTCCTAGGCACAGCTCTAAGCCTCC
```
```
> NC_011137.1 Reversed
GGAGGCTTAGAGCTGTGCCTAGGACTCCAGCTCATGCGCCGAATAGTAGGTATAGTGTTCCAATGTCTTTGTGGTTTGTAGAGAATAGTCAACGGTCGGCGAACAT
```

Code skeleton here: 


### Extract position 20 etc..


### Reformat files, biopython 



### save and upload files from a remote server
SFTP - scp - rsync


