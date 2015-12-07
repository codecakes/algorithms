"""
You are given a square matrix of size N×N. Can you calculate the absolute difference of the sums across the main diagonal and the secondary diagonal?
"""

#!/bin/python

n = int(raw_input().strip())
mat = []
diagMain = 0
diagMinor = 0

# O(N)
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    mat.append(a_temp)

if mat:
    # O(N)
    for index, eachList in enumerate(mat):
        diagMain += eachList[index]
        diagMinor += eachList[(n-1)-index]
    print abs(diagMain-diagMinor)