#!/usr/bin/env ruby

#get argument passed to script
input_string = ARGV[0]

# Define regular expression to match "School"
regex = /School/

# Check if the input_string matches regular expression
#if match_data = input_string.scan(regex)
	#if theres a match, print matched part
#	puts match_data[0]
#else
	#print empty string
#	puts ' '
#end
matches = input_string.scan(regex)
puts matches.join
