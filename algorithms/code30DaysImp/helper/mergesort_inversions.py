#!/usr/bin/python
"""
Insertion Sort is a simple sorting technique which was covered in previous challenges. Sometimes, arrays may be too large for us to wait around for insertion sort to finish. Is there some other way we can calculate the number of times Insertion Sort shifts each elements when sorting an array?

If ki is the number of elements over which the ith element of the array has to shift, then the total number of shifts will be k1 +k2 +...+kN.

Input Format
The first line contains the number of test cases, T. T test cases follow. The first line for each test case contains N, the number of elements to be sorted. The next line contains N integers (a[1], a[2], ..., a[N]).

Output Format
Output T lines containing the required answer for each test case.

Sample Input

2
5
1 1 1 2 2
5
2 1 3 1 2

Sample Output

0
4

Explanation
The first test case is already sorted, therefore there's no need to shift any element. In the second case, it will proceed in the following way.

Array: 2 1 3 1 2 -> 1 2 3 1 2 -> 1 1 2 3 2 -> 1 1 2 2 3
Moves:   -        1       -    2         -  1
"""
def merge_inversion(left, right, inversions):
    left_ln = len(left)
    right_ln = len(right)
    aux = []
    left_i = right_j = 0
    while left_i<left_ln and right_j<right_ln:
        num_left = left[left_i]
        num_right = right[right_j]
        if num_left>num_right:
            # print num_left, num_right
            inversions[0] += 1
        if (num_left<num_right):
            aux.append(num_left)
            left_i += 1
        else:
            aux.append(num_right)
            right_j += 1

    index, slice_arr = (left_i, left) if left_i<left_ln else (right_j, right)
    slice_ln = len(slice_arr)
    while index<slice_ln:
        # print index, slice_arr
        aux.append(slice_arr[index])
        index += 1

    return aux

def mergesort_inversion_iter2(arr, merge_func=merge_inversion):
    '''Iterative top down out of place space intensive merge sort'''
    stack = [arr]
    mergeList= []
    inversions = [0]
    while stack:
        arr = stack.pop()
        ln = len(arr)
        if len(mergeList) > 1:
            mergeList.append(merge_func(mergeList.pop(), mergeList.pop(), inversions))
        if ln > 1:
            mid = ln//2
            # slicing and dicing
            left = arr[:mid]
            stack.append(left)
            right = arr[mid:]
            stack.append(right)
            # print left, right
        else:
            # once its single length array, merge the two
            mergeList.append(arr)
    while len(mergeList) > 1:
        mergeList.append(merge_func(mergeList.pop(), mergeList.pop(), inversions))
    return inversions[0]