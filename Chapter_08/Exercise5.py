__author__ = 'matt'

def count(word, letter):
    """Given a string and a letter,
    return occurence count"""
    return sum(i == letter for i in word)

if __name__ == '__main__':
    print count('racecar', 'c')
    print count('racecar', 'e')
