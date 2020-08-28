#! /usr/bin/env python3

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists

# Check for correct number of arguments
if len(sys.argv) != 3:
    print("Correct usage: wordCount.py <input text file> <output text file>")
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

#make sure text files exist
if not os.path.exists(input_file):
    print ("text file input %s doesn't exist! Exiting" % textFname)
    exit()
    
#make sure output file exists
if not os.path.exists(output_file):
    print ("wordCount output file %s doesn't exist! Exiting" % outputFname)
    exit()

word_dictionary = {}

with open(input_file, "r") as inputfile:
    for line in inputfile:
        # split only when punctuation, whitespace or other characters not in ASCII are found
        words = re.split("[\W+|\s]", line)
        for word in words:
            if word.lower() in word_dictionary:
                word_dictionary[word.lower()] += 1
            else:
                word_dictionary[word.lower()] = 1

del word_dictionary['']

with open(output_file, "w") as outputfile:
    for k, v in sorted(word_dictionary.items()):
        outputfile.write("{0} {1}\n".format(k,v))
