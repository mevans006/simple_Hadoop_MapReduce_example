#!/usr/bin/env python
import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line1 = line.strip()

    # Make all lines lowercase
    line2 = line1.lower()

    # split the line into words; splits on any whitespace
    words = line2.split()

    # Add Stopwords
    stopwords = set(['the', 'and', ',' ,'.', 'i', 'you', 'we'])

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if not word in stopwords:
            print '%s\t%s' % (word, "1")
