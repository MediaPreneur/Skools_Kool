__author__ = 'matt'

def any_lowercase1(s):
    """Return True/False based on case of first letter"""
    for c in s:
        return bool(c.islower())

def any_lowercase2(s):
    """Returns True because string 'c' is lowercase"""
    for c in s:
        return "True" if 'c'.islower() else 'False'

def any_lowercase3(s):
    """Returns result for last letter"""
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        """ Truth Test. flag is assigned a value of True or False based on
        the results of the conditional OR flag; c.islower(). If one value
        evalautes to True, flag is assigned a new boolean value of True"""
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """Cycles through all values, returns True if lowerc-ase"""
    return all(c.islower() for c in s)

if __name__ == '__main__':
    print any_lowercase1('UPPER')
    print any_lowercase2('TrueValue')
    print any_lowercase3('TrueValuE')
    print any_lowercase4('TrueValue')
    print any_lowercase5('trueValue')

