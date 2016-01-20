#!/bin/python
"""
In this challenge, don't print every time you move an element. Instead, print the array after each iteration of the insertion-sort, i.e., whenever the next element is placed at its correct position.

Since the array composed of just the first element is already "sorted", begin printing from the second element and on.

Input Format
There will be two lines of input:

    s - the size of the array
    ar - a list of numbers that makes up the array

Output Format
On each line, output the entire array at every iteration.


Sample Input

6
1 4 3 5 6 2

Sample Output

1 4 3 5 6 2
1 3 4 5 6 2
1 3 4 5 6 2
1 3 4 5 6 2
1 2 3 4 5 6

Explanation
Insertion Sort checks 4 first and doesn't need to move it, so it just prints out the array. Next, 3 is inserted next to 1, and the array is printed out. This continues one element at a time until the entire array is sorted.

Task
The method insertionSort takes in one parameter: ar, an unsorted array. Use an Insertion Sort Algorithm to sort the entire array.
"""

def swap(ar, index, preindex):
    ar[index], ar[preindex] = ar[preindex], ar[index]

def insertionSort(ar):
    size = len(ar)
    for i in xrange(size):
        j = i
        if j>0:
            while (j>0 and ar[j] < ar[j-1]):
                swap(ar, j, j-1)
                j -= 1
            print ' '.join(map(str, ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)