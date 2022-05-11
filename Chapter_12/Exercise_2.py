__author__ = 'matt'

"""
In this example, ties are broken by comparing words, so words with the same length appear in reverse alphabetical order. For other applications you might want to break ties at random. Modify this example so that words with the same length appear in random order. Hint: see the random function in the random module. Solution: http://thinkpython.com/code/unstable_sort.py.
"""

from random import random

def sort_by_length(words):
    t = [(len(word), random(), word) for word in words]
#        t.append((random(),len(word), word))

    # For a tuple, sort occurs based on elements from left to right
    t.sort(reverse=True)

    return [word for length, dupsort, word in t]

if __name__ == '__main__':
    sortSequence = ('cat','rat','matt','fence','hair','chair')
    print sort_by_length(sortSequence)
