#!/usr/bin/perl

use strict;
use warnings;

open IN, "solution_2.2.txt" or die ("\ncannot open: solution_2.2.txt, please check that this file exists\n\n");
while (my $line = <IN>) {
	chomp $line;
	if ($line =~ /Please give me solution 2.2/) {
		my $char = chr(78);
		print "\nYour file was found to contain the correct phrase. Bravo!\nThe sixth character is $char\n\n";
	}
	else {
		print "\nSorry the correct phrase 'Please give me solution 2.2' was not detected.\nCheck the spelling carefully and try again\n\n";
	}
}
