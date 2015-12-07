"""
Input
You are given an integer N depicting the height of the staircase.

Output
Print a staircase of height N that consists of # symbols and spaces. For example for N=6, here's a staircase of that height:

     #
    ##
   ###
  ####
 #####
######

"""
n = int(raw_input().strip())

for num in xrange(1,n+1):
    print ('#'*num).rjust(n)