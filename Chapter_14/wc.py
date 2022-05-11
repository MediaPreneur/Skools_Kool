__author__ = 'matt'
"""
Type this example into a file named wc.py and run it as a script. Then run the Python interpreter and import wc. What is the value of __name__ when the module is being imported?
"""
import os, sys

def linecount(filename):
    return sum(1 for _ in open(filename))

if __name__=='__main__':
    # Use sys.path.insert to add directory to python path
    sys.path.insert(0,'/home/matt/projects/Skools_Kool/Chapter_14/')
    print __name__
    import wc
    print __name__
    print os.getcwd()
    print linecount('/home/matt/projects/Skools_Kool/Chapter_14/wc.py')
