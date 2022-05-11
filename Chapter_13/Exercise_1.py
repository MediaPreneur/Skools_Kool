__author__ = 'matt'

"""
Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.
Hint: The string module provides strings named whitespace, which contains space, tab, newline, etc., and punctuation which contains the punctuation characters.
"""

import string

def stringer(fin):
    """Return an otherwise unreadable string from a file."""
    try:
        myFile = open(fin, 'r')
        return ''.join(
            string.lower(char)
            for char in myFile.read()
            if char not in string.whitespace and char not in string.punctuation
        )

    except:
        return e
    finally:
        myFile.close()

if __name__ == '__main__':
    infile = '/Users/matt/Documents/PyCharm/Skools_Kool/Chapter_13/testtext.txt'
    print stringer(infile)
