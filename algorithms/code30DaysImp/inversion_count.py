#!/usr/bin/python

from array import array

def count_split_inv(arr, left_lo, left_hi, right_lo, right_hi):
    # initialize vars
    arr_ln = right_hi - left_lo + 1
    aux = array('i', [0]*(arr_ln))
    left_i = left_lo
    right_j = right_lo
    inv = 0
    index = 0

    # print left_i, left_hi, right_j, right_hi
    # print arr[left_i:left_hi+1], arr[right_j:right_hi+1]
    # fill in the aux array with corre
    while left_i <= left_hi and right_j <= right_hi:
        if arr[left_i] <= arr[right_j]:
            aux[index] =  arr[left_i]
            index += 1
            left_i += 1
        else:
            # this condition means A[i] > A[j] while i<j so this is an inversion
            # all elements i and above indices will be greater than element at j
            inv += left_hi - left_i + 1
            aux[index] = arr[right_j]
            index += 1
            right_j += 1

    # print "inv %s"%(inv)
    # fill in rest with correct order smallest array first
    while left_i<=left_hi:
        aux[index]= arr[left_i]
        left_i += 1
        index += 1
    # then bigger a
    while right_j<= right_hi:
        aux[index]= arr[right_j]
        right_j += 1
        index += 1
    # overwrite the indices in original arr with new sorted array
    for i in xrange(right_hi - left_lo +1):
        arr[i+left_lo] = aux[i]
    return inv


def count_split(arr, lo, hi):
    if lo<hi:
        # split array in half
        mid = (lo+hi)/2
        # find count inversions in left half
        l_c = count_split(arr, lo, mid)
        # print l_c
        #find count inversions in right half
        r_c = count_split(arr, mid+1, hi)
        # print r_c
        # find count inversions between the two arrays
        split_c = count_split_inv(arr, lo, mid, mid+1, hi)
        # print split_c
        return l_c+r_c+split_c
    else:
        return 0


if __name__ == "__main__":
    n = input()
    for iterate in range( n ):
        x = input()
        # a = array('i', [ int( i ) for i in raw_input().strip().split() ])
        a = [ int( i ) for i in raw_input().strip().split() ]
        print count_split(a, 0, len(a)-1)
