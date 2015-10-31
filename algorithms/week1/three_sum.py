"""
Given a list of numbers and an argument,
find the sets of 3 numbers that equals the argument, which is a number.

1. Sort the list
2. For each number,
    - iterate and couple with rest of numbers
    - find its sum
    If the argument is ZERO.
    - do a binary search and find the negative in the rest of list
    Else for any other argument
    - do a binary search and find the difference of argument and sum
"""

def binary_search(key, alist):
    ln = len(alist)
    lo,hi = 0, ln-1

    while ( lo <= hi ):
        mid = (lo+hi)/2
        #print "mid is %s" %mid
        if key < alist[mid]:
            hi = mid
        elif key > alist[mid]:
            lo = mid+1
        else:
            return alist[mid]

    if lo == hi and alist[lo] == key:
            return key
    return None


def three_sum(setList, resultNum):
    sets = set()
    sortedList = sorted(setList)
    ln = len(sortedList)

    #O(N^2 lgN)
    for eachIndex in xrange(ln):
        for eachIndex2 in xrange(ln):
            if eachIndex2 != eachIndex:
                res = sortedList[eachIndex] + sortedList[eachIndex2]
                #print "%s + %s = %s" %(sortedList[eachIndex], sortedList[eachIndex2], res)
                #lg(N)
                #print "-res = %s" %(-res)
                op = binary_search(-res, sortedList)
                if op:
                    if op+res == resultNum:
                        sets.add((sortedList[eachIndex], sortedList[eachIndex2], -res))
    return sets

#For debugging purpose only
if __name__ == "__main__":
    sample = [40, -10, -30, -10, 50, 20, 60, -70]
    srtList = sorted(sample)
    print "sorted list %s" %srtList
    for each in sample:
        print binary_search( each, srtList )
    print binary_search( -600, srtList )
    print binary_search( 1000, srtList )
    print three_sum(sample, 0)
