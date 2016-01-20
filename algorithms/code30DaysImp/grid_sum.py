#!/bin/python

"""
Given a 6x6 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We can find 16 hourglasses in A; we define an hourglass in A to be a subset of values with indexes falling in this pattern in A's graphical representation:

a b c
  d
e f g

The sum of an hourglass is the sum of the values within it.

Your task is to calculate the sum of every hourglass in some 2D Array, A, and print the largest value (maximum of the sums) as your answer.

Input Format



Output Format

Print the largest (maximum) hourglass sum found in A.

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output

19

Explanation

Sample Input A contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

The hourglass with the maximum sum (19) is:

2 4 4
  2
1 2 4

"""

def find_sum(A, lo, hi, max_ln, slice_window):
    if not (max_ln-lo >= slice_window): return
    # print "A[lo]={}, lo={}, max_ln={}".format(A[lo], lo, max_ln)
    arr=A[lo]
    mid_arr = A[lo+1]
    base_arr = A[lo+2]
    max_arr_sum = float('-inf')
    # O(n)
    for index in xrange(len(arr)-slice_window+1):
        index_end = index + slice_window
        res = sum(arr[index:index_end]) + mid_arr[index+1] + sum(base_arr[index:index_end])
        # print res
        # print "="*10
        if res > max_arr_sum: max_arr_sum = res
    return max_arr_sum

def arr_split_max_sum(A, slice_window=3):
    '''Iteratively split Array to single slices and find hour glass sum'''
    max_ln = hi = len(A)
    mid = lo = 0
    stack = [(lo, hi)]
    max_sum = float('-inf')
    # lg(n)
    while (stack):
        lo, hi = stack.pop()
        mid = (lo+hi)/2
        if lo<hi and lo!=mid and hi!=mid:
            left, right = A[lo:mid], A[mid:hi]
            stack.append((lo, mid))
            stack.append((mid, hi))
        else:
            res = find_sum(A, lo, hi, max_ln, slice_window)
            # print res
            if res > max_sum: max_sum = res
    return max_sum

if __name__ == "__main__":
    A= [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
        ]
    # print arr_split_max_sum(A)
    assert arr_split_max_sum(A) == 19