#!/bin/python

"""
Your teacher has given you the task of drawing a staircase structure. Being an expert programmer, you decided to make a program to draw it for you instead. Given the required height, can you print a staircase as shown in the example?
Note: The last line has zero spaces before it.

Good luck!

Constraints
1≤N≤100

Input Format

You are given an integer N depicting the height of the staircase.

Output Format

Print a staircase of height N that consists of # symbols and spaces as given in Sample Output.

Sample Input

6

Sample Output

     #
    ##
   ###
  ####
 #####
######

"""

import sys


n = int(raw_input().strip())

s = '#'
for i in xrange(1,n+1):
    print (s*i).rjust(n) #zfill(n).replace('0',' ')