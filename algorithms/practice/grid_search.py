#!/bin/python

"""
Given a 2D array of digits, try to find the location of a given 2D pattern of digits. For example, consider the following 2D matrix:

1234567890
0987654321
1111111111
1111111111
2222222222
Assume we need to look for the following 2D pattern:

876543
111111
111111

If we scan through the original array, we observe that the 2D pattern begins at the second row and the third column of the larger grid (the 8 in the second row and third column of the larger grid is the top-left corner of the pattern we are searching for).

So, a 2D pattern of P digits is said to be present in a larger grid G, if the latter contains a contiguous, rectangular 2D grid of digits matching with the pattern P, similar to the example shown above.

Input Format
The first line contains an integer, T, which is the number of test cases. T test cases follow, each having a structure as described below:
The first line contains two space-separated integers, R and C, indicating the number of rows and columns in the grid G, respectively.
This is followed by R lines, each with a string of C digits, which represent the grid G.
The following line contains two space-separated integers, r and c, indicating the number of rows and columns in the pattern grid P.
This is followed by r lines, each with a string of c digits, which represent the pattern P.

Constraints
1≤T≤5
1≤R,r,C,c≤1000
1≤r≤R
1≤c≤C

Sample Input

2
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99
Sample Output

YES
NO
"""

import sys


def search(mat, pattern, C, r, c, limit, lo, global_mat):
    '''
    - select middle row
    - iterate row with slice, c
    - if pattern found, iterate through r rows finding pattern at each stage
    - return true if found
    '''
    middle_row = mat[0]
    # print middle_row
    i = 0
    k = 0
    flag= False
    res = middle_row
    #only detecting one pass of pattern, not multiple - when count overflows r i.e. count == r break out;
    count = 0
    while (i<C and k < r):
        block = middle_row[i:i+c]
        # print "block is %s, pattern is %s, k %s r %s" %(block, pattern[k], k, r)
        if block == pattern[k] and lo+k+1 < limit:
            k += 1
            middle_row = global_mat[lo+k]
            flag = True
            count += 1
        else:
            i += 1
            k = 0
            flag = False
            middle_row = res
        if count == r: break
    return flag


def search_divide(mat, pattern, C, r, c, limit, lo=0, hi=None, global_mat=None):
    '''
    - slice by row;
    - search each row iteratively for pattern
    - if found the first row, check rest of row below it for a block-match;
    - Return True if found

    mat: A list of N lists (NxN matrix)
    R: Total rows
    C: Total Colums
    r: pattern rows
    c: pattern cols
    limit: upper limit of original matrix
    lo: lower index point of mat
    hi: upper index point of mat
    global_mat: original matrix
    '''
    #divide
    mid = (lo+hi)/2
    #print lo, mid, hi
    if mid>0 and lo<hi and mid!=lo:
        new_r = mid
        left = global_mat[lo:new_r]
        right = global_mat[new_r:hi]
        # print "left, lo %s hi %s %s" %(lo, new_r, left)
        # print "right, lo %s hi %s %s" %(new_r, hi, right)
        left = (search_divide(left, pattern, C, r, c, limit, lo = lo, hi=new_r, global_mat=global_mat))
        right = (search_divide(right, pattern, C, r, c, limit, lo=new_r, hi=hi, global_mat=global_mat))
        return left or right
    else:
        # print global_mat[lo:hi]
        return search(mat, pattern, C, r, c, limit, lo, global_mat)
        # print "lo %s hi %s" %(lo, hi)


## test - following works

# grand, pat, R, C, pr, pc = [[7, 2, 8, 3, 4, 5, 5, 8, 6, 4], [6, 7, 3, 1, 1, 5, 8, 6, 1, 9], [8, 9, 8, 8, 2, 4, 2, 6, 4, 3], [3, 8, 3, 0, 5, 8, 9, 3, 2, 4], [2, 2, 2, 9, 5, 0, 5, 8, 1, 3], [5, 6, 3, 3, 8, 4, 5, 3, 7, 4], [6, 4, 7, 3, 5, 3, 0, 2, 9, 3], [7, 0, 5, 3, 1, 0, 6, 6, 0, 1], [0, 8, 3, 4, 2, 8, 2, 9, 5, 6], [4, 6, 0, 7, 9, 2, 4, 1, 3, 7]], [[9, 5, 0, 5], [3, 8, 4, 5], [3, 5, 3, 0]], 10, 10, 3, 4

# print 'YES' if search_divide(grand, pat, C, pr, pc, R, lo=0, hi = R, global_mat=grand) else 'NO'

from collections import defaultdict

tests = int(raw_input())
mat = []
grand_mat = defaultdict(dict)
pmat = []
pattern_mat = []

count = 0
for each_test in xrange(tests):
    # Collect all rows of the Grand Matrix
    R,C = map(int, raw_input().strip().split(' '))
    for each_row in xrange(R):
        row = map(int, list(raw_input().strip()))
        mat.append(row)
    grand_mat.setdefault(count, {}).update({'g': mat, 'row': R, 'col': C})
    mat = []

    # Collect all rows of the pattern Matrix
    pr,pc = map(int, raw_input().strip().split(' '))
    for each_row in xrange(pr):
        row = map(int, list(raw_input().strip()))
        pmat.append(row)
    grand_mat.setdefault(count, {}).update({'p': pmat, 'pr': pr, 'pc': pc})
    pmat = []

    count += 1


for each_matrix in xrange(tests):
    grand = grand_mat[each_matrix]['g']
    pat = grand_mat[each_matrix]['p']
    R = grand_mat[each_matrix]['row']
    C = grand_mat[each_matrix]['col']
    pr = grand_mat[each_matrix]['pr']
    pc = grand_mat[each_matrix]['pc']
    # print grand, pat, R, C, pr, pc
    print 'YES' if search_divide(grand, pat, C, pr, pc, R, lo=0, hi = R, global_mat=grand) else 'NO'
