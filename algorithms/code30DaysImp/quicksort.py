#!/bin/python

def swap(findex, sindex, ar):
    ar[findex], ar[sindex] = ar[sindex], ar[findex]

def partition(ar, lo, hi):
    '''3 way djisktra partition method'''
    start = lo
    pivotIndex = (lo+hi)//2
    # take the elemet @ hi as the pivot and swap it to pivotIndex position
    swap(pivotIndex, hi, ar)
    pivotIndex = hi
    pivot = ar[pivotIndex]
    eq = lo
    for index in xrange(lo, hi):
        if (ar[eq] == pivot):
            eq += 1
        if (ar[index] < pivot and index < pivotIndex):
            swap(index, lo, ar)
            lo += 1
            eq +=1
    swap(lo, pivotIndex, ar)
    return lo

def quickSort(ar):
    '''Iterative unstable in-place sort'''
    n = len(ar)
    hi = n-1
    lo = 0
    stack = [(lo, hi)]
    while stack:
        lo, hi = stack.pop()
        pivot = partition(ar, lo, hi)
        if lo<pivot-1:
            stack.insert(0, (lo, pivot-1))
        if pivot+1<hi:
            stack.insert(0, (pivot+1, hi))

def quickSortRec(ar, n, lo, hi):
    '''Recursive unstable in-place sort'''
    pivot = partition(ar, lo, hi)
    # print lo, pivot, hi
    if lo<pivot-1 and lo != pivot:
        quickSortRec(ar, n, lo, pivot-1)
        # print ' '.join(ar)
    if pivot+1<hi and pivot != hi:
        quickSortRec(ar, n, pivot+1, hi)
        # print ' '.join(ar)