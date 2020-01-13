#!/usr/bin/perl

use strict;
use warnings;

my $arg = $ARGV[0];
chomp $arg;

if ($arg == 36) {
	my $char1 = chr(78);
	my $char2 = chr(69);
	print "\nWell done! The last 2 characters are $char1 and $char2\n\n";
}

else {
	print "\nSorry $arg is not the correct number of line. Try again\n\n";
}