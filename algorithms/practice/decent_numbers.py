"""
Problem Statement

Sherlock Holmes suspects his archenemy, Professor Moriarty, is once again plotting something diabolical. Sherlock's companion, Dr. Watson, suggests Moriarty may be responsible for MI6's recent issues with their supercomputer, The Beast.

Shortly after resolving to investigate, Sherlock receives a note from Moriarty boasting about infecting The Beast with a virus; however, he also gives him a clue—a number, N. Sherlock determines the key to removing the virus is to find the largest Decent Number having N digits.

A Decent Number has the following properties:

Its digits can only be 3's and/or 5's.
The number of 3's it contains is divisible by 5.
The number of 5's it contains is divisible by 3.
Moriarty's virus shows a clock counting down to The Beast's destruction, and time is running out fast. Your task is to help Sherlock find the key before The Beast is destroyed!

Constraints
1≤T≤20
1≤N≤100000


Input Format

The first line is an integer, T, denoting the number of test cases.

The T subsequent lines each contain an integer, N, detailing the number of digits in the number.

Output Format

Print the largest Decent Number having N digits; if no such number exists, tell Sherlock by printing -1.

Sample Input

4
1
3
5
11
Sample Output

-1
555
33333
55555533333
Explanation

For N=1, there is no such number.
For N=3, 555 is the only possible number.
For N=5, 33333 is the only possible number.
For N=11, 55555533333 and all permutations of these digits are valid numbers; among them, the given number is the largest one.
"""

def decent_num(n):
    if n<3: return -1
    if 3<n<5:
        res = 3
        res2 = 5
    else:
        res = 5
        res2 = 3
    j = 0
    # find the remainder from dividend, n and divider, res=3 or 5
    rem = n-(res*j)
    # while rem is not divisible by divider, keep incrementing j
    while (rem%res2 != 0 and j<n/res):
        j += 1
        rem = n-(res*j)
    # get fives and three's multiple
    fives_multiple = 5 * j
    threes_multiple = rem
    # print "n- %s: fives_multiple %s mod 5 %s and threes_multiple %s mod 3 %s" %(n, fives_multiple, fives_multiple%5, threes_multiple, threes_multiple%3)
    if (fives_multiple%5 == 0) and (threes_multiple%3 == 0):
        return int(('5'*threes_multiple)+('3'*fives_multiple))
    return -1

# In the original solution I've included following
'''
tests = int(raw_input().strip())
if 1<=tests<=20:
    for a0 in xrange(tests):
        N = int(raw_input().strip())
        if 1<=N<=100000:
            print decent_num(N)
'''

# for testing and debugging purpose only

test = [-1, -1, -1, 555, -1, 33333, 555555, -1, 55533333, 555555555, 3333333333, 55555533333]
for i in xrange(12):
    assert decent_num(i) == test[i]

test = [1, 2, 10, 100, 100, 200, 1, 1, 1, 1]
ans = [-1, -1, 3333333333, 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555553333333333, \
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555553333333333, \
        55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555533333, \
        -1, -1, -1, -1]

assert decent_num(100) == 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555553333333333
assert decent_num(200) == 55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555533333

for i in xrange(len(test)):
    assert decent_num(test[i]) == ans[i]

