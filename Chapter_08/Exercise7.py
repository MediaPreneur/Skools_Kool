__author__ = 'matt'

from string import count

def countMe(s, sub, start=None, end=None):
    """Mimic functionality of string.count() method"""
    # Test for values in star/end
    if end is None:
        end = len(s)

    index = 0 if start is None else start
    countMeCount = 0
    while index < end:
        if s[index]==sub:
            countMeCount+=1
        index+=1
    return countMeCount

if __name__ == '__main__':
    print countMe('racecar','c',2,5)

