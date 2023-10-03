#!/usr/bin/env ruby

#get argument passed to script
input_string = ARGV[0]

# Define regular expression to match "School"
regex = /hb(t{n+}n)/

# Use scan method to find all the matches in the input string
matches = input_string.scan(regex)

# Print matched parts concatenated together
puts matches.join
