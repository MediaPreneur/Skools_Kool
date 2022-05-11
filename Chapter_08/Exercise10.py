__author__ = 'matt'

def is_palindrome(word):
    return word == word[::-1]

if __name__ == '__main__':
    print is_palindrome('amazon')
    print is_palindrome('racecar')
