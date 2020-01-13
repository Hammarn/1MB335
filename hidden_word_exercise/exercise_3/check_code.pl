#!/usr/bin/perl

use strict;
use warnings;

my $dirname = 'solution';
my $filename = 'solution/codes.txt';

if (! -d $dirname) {
	print "\nSorry the directory 'solution' is not there\n";
}

elsif (! -e $filename) {
	print "\nSorry the file 'codes.txt' was not found in the directory 'solution'\n";
}

else {
	open IN, "$filename" or die ("cannot open $filename");
	print "\nGood job! The next 2 characters are:\n\n";
	while (my $line = <IN>) {
		chomp $line;
#		print "$line\n";
		my $character = chr($line);
		print "$character\n";
	}
}

print "\n";
