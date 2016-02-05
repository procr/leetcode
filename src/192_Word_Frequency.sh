#!/bin/bash
# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt \
	| tr -s ' ' '\n' \
	| awk '{nums[$1]++} END {for(word in nums) print word, nums[word]}' \
	| sort -rn -k2	
