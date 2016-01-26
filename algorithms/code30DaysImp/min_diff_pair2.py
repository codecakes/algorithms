# This seems to be a better approach to solving absolute min differences problems
# sort the array first
# Then filter out pairs of abs min diff out of the lot

from array import array

"""
The absolute difference between two integers, a and b, is |a−b|. The minimum absolute difference between two integers in a list A of positive integers, is the smallest absolute difference between any two integers in A.

Given a list A={a0,a1,…,aN−1} of unsorted integers, find and print the pair (or pairs) of elements having the minimum absolute difference.

Note: More than one pair of elements may have the same absolute difference.

Input Format

The first line contains a single integer N, denoting the length of list A.
The second line contains N space-separated integers, a0,a1,…,aN−1, representing the elements in A.

Constraints

    2≤N≤2×105
    −107≤Ai≤107
    Ai≠Aj,where 0≤i<j≤N−1

Output Format

Print the space-separated pair of elements having the minimum absolute difference in ascending order. If more than one pair meets this criterion, print them consecutively, separated by a space, in ascending order on a single line. Because we are printing space-separated pairs, some elements may appear more than once in your output.

Sample Input 1

10
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854

Sample Output 1

-20 30

Explanation
The minimum absolute difference is 50 (ABS(30−(−20))=50). The only pair having this difference is (−20,30).

Sample Input 2

12
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470

Sample Output 2

-520 -470 -20 30

Explanation
Our minimum absolute difference is 50. The pairs (−470,−520) and (−20,30) both have this difference.

Sample Input 3

4
5 4 3 2

Sample Output 3

2 3 3 4 4 5

Explanation
Our minimum absolute difference is 1. The pairs (2,3), (3,4), and (4,5) all have this difference. Notice that 3 and 4 appear multiple times, because they are components of more than one pair.

Note: Recall that pairs in the output must be printed in ascending order.
"""

## This is merge
def merge(arr, left_lo, left_hi, right_lo, right_hi):
    # initialize vars
    arr_ln = right_hi - left_lo + 1
    aux = array('i', [0]*(arr_ln))
    left_i = left_lo
    right_j = right_lo
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
            aux[index] = arr[right_j]
            index += 1
            right_j += 1

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

# This is merge sort
def merge_split(arr, lo, hi):
    if lo<hi:
        # split array in half
        mid = (lo+hi)/2
        merge_split(arr, lo, mid)
        merge_split(arr, mid+1, hi)
        merge(arr, lo, mid, mid+1, hi)
        # print split_c
        return

abs_diff = lambda x,y: abs(x-y)

def count_min_diff(arr):
    '''Count the total minimum differences and filter out the abs min diff pairs'''
    diff_pair = []
    ln = len(arr)
    lo = 0
    hi = ln-1
    _min = float('inf')
    # O(lgN)
    merge_split(arr, lo, hi)
    # O(N)
    for index in xrange(ln-1):
        res = abs_diff(arr[index], arr[index+1])
        if res <= _min:
            _min = res
            diff_pair.append((arr[index], arr[index+1], res))
    return ' '.join([' '.join([str(a),str(b)]) for a,b,c in diff_pair if c == _min])

N = int(raw_input())

arr = array('i', map(int, raw_input().strip('\n').split()))

print count_min_diff(arr)