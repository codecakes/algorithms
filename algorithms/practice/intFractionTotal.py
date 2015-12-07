#!/bin/python

"""
Problem Statement

You're given an array of integers. Can you find what fraction of the elements are positive numbers, negative numbers and zeroes? Print the value of the fractions in decimal form with 3 decimal places.

Input Format

The first line contains N: the size of the array.
The next line contains N space-separated integers A1,A2,A3,⋯,AN.

Output Format

Output the three values each on a different line. The first value shows the fraction of the count of positive numbers to the total numbers, the second shows the fraction of negative numbers, and the third represents the fraction of zeroes. Correct the fraction to 3 decimal places.

Sample Input

6
-4 3 -9 0 4 1
Sample Output

0.500
0.333
0.167
Explanation

There are 3 positive numbers, 2 negative numbers and 1 zero in the array.
The fraction of the positive numbers, negative numbers and zeroes are 36=0.500, 26=0.333 and 16=0.167 respectively.

Note: This challenge introduces precision problems. You can even print the output to 4 decimal places and above, but only the difference at the 3rd decimal digit is noted. That is the reason you'll notice testcases have much higher precision (more decimal places) than required.
Answers with absolute error up to 10−4 will be accepted.
"""


n = int(raw_input().strip())

pos_count = neg_count=zeroes = num = 0
fraction = lambda x,n: round(float(x)/n, 6)

for each_num in raw_input().strip().split(' '):
    num = int(each_num)
    if num > 0: pos_count += 1
    if num < 0: neg_count += 1
    if num == 0: zeroes += 1

for frac in [fraction(pos_count, n), fraction(neg_count, n), \
                fraction(zeroes, n)]:
    print frac