#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Read text paragraph by paragraph to JSON.

import sys
import json

# Pass the argument to filename
filename = sys.argv[-1]
file_export = filename + ".json"

# If no filename is given terminate the program
if filename == "./para2json.py":
	print
	print "Usage: ./para2json.py filename.txt"
	print
	sys.exit()

par_separator = "\n\n"
counter = 0

# Reading the text file to be processed.
print "Loading text..."
with open(filename, 'r') as text_file:
    text = text_file.read()

paragraphs = text.split(par_separator)

for paragraph in paragraphs:
    counter = counter + 1
    id_name = filename + "." + str(counter)
    try:
        data = {
            'id' : id_name,
            'series' : filename,
#    'title' : doc['pageOCRData']['metadata']['title'],
#    'date' : doc['pageOCRData']['metadata']['published']['#text'],
#    'lang' : doc['pageOCRData']['metadata']['language'],
            'text' : paragraph.replace('\n', ' ')
        }
    except KeyError:
        data = {
            'id' : id_name,
            'series' : filename,
            'text' : ''
        }
    with open(file_export,'a') as outfile:
        json.dump(data, outfile, sort_keys=False)
        outfile.write('\n')
    outfile.close()
    data = {}
