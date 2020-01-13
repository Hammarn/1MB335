#!/usr/bin/perl

use strict;
use warnings;

my $filename = 'junk.txt';

if (-e $filename) {
	print "\n\nSorry, the file 'junk.txt' is still there\n";
}
 else {
 	my $char = chr(76);
 	print "\nYeah the junk file has been deleted!\nThe nineth character of the solution is $char\n";
 }

opendir (DIR, 'data') or die "$!";
readdir DIR;
readdir DIR;
if (readdir DIR) { #now there should be a file or folder
  print "\nSorry the 'data' directory still contains some files\n";
}
else {
   my $char = chr(73);
   print "\nYeah the data directory is empty.\nThe tenth character of the solution is $char\n\n";
}