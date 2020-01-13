#!/usr/bin/perl

use strict;
use warnings;

print "\nPlease enter the size of the text file (in bytes): ";
my $size = <STDIN>;
chomp $size;

if (($size == 65) | ($size == 66) | ($size == 67) ) {
	print "\nCorrect! The fourth character is M.\n\n";
}

else {
	print "Sorry, please try again.\n\n";
}
