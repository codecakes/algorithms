# This is performant but somewhat yields wrong answers during last 2 test cases
# in Hackerrank's All Contests>30 Days of Code > Day 16: Sorting!

from array import array

abs_diff = lambda x,y: abs(x-y)

def set_diff(x,y, diff):
    res = abs_diff(x, y)
    if res <= diff: diff = res
    return diff

def count_split_min_pair(arr, diff_pair, left_lo, left_hi, right_lo, right_hi):
    # initialize vars
    arr_ln = right_hi - left_lo + 1
    aux = array('i', [0]*(arr_ln))
    left_i = left_lo
    right_j = right_lo
    diff = float('inf')
    index = 0

    # print left_i, left_hi, right_j, right_hi
    # print arr[left_i:left_hi+1], arr[right_j:right_hi+1]
    # fill in the aux array with corre
    while left_i <= left_hi and right_j <= right_hi:
        if arr[left_i] <= arr[right_j]:
            aux[index] =  arr[left_i]
            # count the least abs difference and add that pair into the list
            diff = set_diff(arr[left_i], arr[right_j], diff)
            diff_pair.append((arr[left_i], arr[right_j], diff))
            left_i += 1
        else:
            # this condition means A[i] > A[j] while i<j so this is an inversion
            # all elements i and above indices will be greater than element at j
            aux[index] = arr[right_j]
            # count the least abs difference and add that pair into the list
            diff = set_diff(arr[left_i], arr[right_j], diff)
            diff_pair.append((arr[right_j], arr[left_i] , diff))
            right_j += 1
        index += 1

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
    return


def count_split(arr, diff_pair, lo, hi):
    if lo<hi:
        # split array in half
        mid = (lo+hi)/2
        # find minimum pairs in left half
        count_split(arr, diff_pair, lo, mid)
        # find minimum pairs in right half
        count_split(arr, diff_pair, mid+1, hi)
        # find minimum pairs between the two arrays
        count_split_min_pair(arr, diff_pair, lo, mid, mid+1, hi)
        return
    else:
        return

# O(lgN+k) ~= O(lgN)
def count_min_diff(arr):
    '''Count the total minimum differences and filter out the abs min diff pairs'''
    diff_pair = []
    ln = len(arr)
    lo = 0
    hi = ln-1
    _min = float('inf')
    pairs = []
    # O(lgN)
    count_split(arr, diff_pair, lo, hi)
    if diff_pair:
        # print diff_pair
        # O(k<<N)
        diff_pair = sorted(diff_pair, key=lambda x: x[2])
        # O(k<<N)
        for each in diff_pair:
            # print each
            a,b,c = each
            if c <= _min:
                _min = c
                pairs.append((a,b,c))
    return ' '.join([' '.join([str(a), str(b)]) for a,b,c in sorted(pairs) if _min==c ]) # # O(m < k <<N)


N = int(raw_input())

arr = map(int, raw_input().strip('\n').split())

print count_min_diff(arr)