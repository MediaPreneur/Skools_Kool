__author__ = 'matt'
import bisect

def bisectFunc(inList, val):
    """Take a sorted list and target value, return the index of the value if exists.
    I guess this means the index in the sorted list, so you can use it for something."""
    searchIndex = bisect.bisect(inList, val)
    try:
        return next(
            (
                'Found at Index: %d' % i
                for i in range(searchIndex - 1, searchIndex + 1)
                if inList[i] == val
            ),
            False,
        )

    except IndexError:
    # IndexError can occur if searched element does not exist and would also occur at end of list.
        return False

if __name__ == '__main__':
    listOne = ['a','b','c','d','e','e','f']
    sortedList = sorted(listOne)
    print bisectFunc(listOne, 'f')
    listTwo = ['f','a','e','c','e','d','b']
    print bisectFunc(sorted(listTwo),'f')
