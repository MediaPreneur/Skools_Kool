# coding=utf-8
__author__ = 'matt'

def avoids(word, bad_letters):
    """Take a word, and return True if
        word doesn't contain any forbidden letters"""
    # Using while loop
    i = 0
    while i < len(word):
        if word[i] in bad_letters:
            return False
        else:
            i+=1
    return True

def avoids_RawInput(in_file):
    """Prompt User Input for forbidden letter list
    check against word list"""
    bad_letters = raw_input('bad letters >>>').split(',')
    fin = open(in_file, 'r')

    return sum(bool(avoids(line.strip(), bad_letters)) for line in fin)

# Exercise 4
def uses_only(word, only_letters):
    """Write a function named uses_only that takes a word and a string of letters, and that returns True if the word contains only letters in the list. Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa?”"""
    i = 0
    while i <len(word):
        if word[i] in only_letters:
            i+=1
        else:
            return False
    return True

# Exercise 5
def uses_all(word, required_letters):
    """Write a function named uses_all that takes a word and a string of required letters, and that returns True if the word uses all the required letters at least once."""
    return all(letter in word for letter in required_letters)

# Exercise 6
def is_abcedarian(word):
    """Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok)."""
    splitter = list(word)
    sorted = sorted(splitter)
    return splitter == sorted


if __name__ == '__main__':
    #bad_letters = ['a','c','d']
    #print avoids('june', bad_letters)
    #print avoids('jam',bad_letters)
    #print avoids_RawInput('words2.txt')
    #print uses_only('racecar',['r','a','c','e'])
    #print uses_only('racecar',['z'])
    #print uses_all('racecar',['r','a'])
    #print uses_all('racecar',['r','a','z'])
    print is_abcedarian('abcxyz')
    print is_abcedarian('ztxe')