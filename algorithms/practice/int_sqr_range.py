"""
Problem Statement

Watson gives two integers (A and B) to Sherlock and asks if he can count the number of square integers between A and B (both inclusive).

Note: A square integer is an integer which is the square of any integer. For example, 1, 4, 9, and 16 are some of the square integers as they are squares of 1, 2, 3, and 4, respectively.

Input Format
The first line contains T, the number of test cases. T test cases follow, each in a new line.
Each test case contains two space-separated integers denoting A and B.

Output Format
For each test case, print the required answer in a new line.

Constraints
1<=T<=100
1<=A<=B<=109

Sample Input

2
3 9
17 24
Sample output

2
0
Explanation
Test Case #00: In range [3,9], 4 and 9 are the two square numbers.
Test Case #01: In range [17,24], there are no square numbers.
"""

from math import floor

def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n < x:
        high *= 2
    low = high/2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

def perfect_sqrs_count(a,b):
    count = 0
    num = 0
    if a==b:
        num = pow(b,0.5)
        a_sqr_root = floor(pow(a,0.5)) if len(str(a)) < 10 else floor(find_invpow(a, 2))
        return 1 if a_sqr_root == num else 0

    b_sqr_root = floor(pow(b,0.5)) if len(str(b)) < 10 else floor(find_invpow(b, 2))
    a_sqr_root = floor(pow(a,0.5)) if len(str(a)) < 10 else floor(find_invpow(a, 2))
    diff = b_sqr_root-a_sqr_root

    if diff>0:
        num = a_sqr_root
        while num<=b_sqr_root:
            res = num*num
            if res == int(res) and a<=res<=b:
                count += 1
            num += 1
    return count

if __name__ == "__main__":
    import sys
    # t = int(raw_input())
    const = 10**9
    fname = sys.argv[1]
    ans = sys.argv[2]
    with open(ans) as fans:
        with open(fname) as f:
            t = int(f.readline().strip().strip('\n'))
            if 1<=t<=100:
                for _ in xrange(t):
                    # a,b = map(int, raw_input().split())
                    a,b = map(int, f.readline().strip().strip('\n').split())
                    output = int(fans.readline().strip().strip('\n'))
                    if 1<=a<=b<=const:
                        try:
                            assert perfect_sqrs_count(a,b) == output
                        except AssertionError as e:
                            print "Range is %s - %s" %(a,b)
                            print perfect_sqrs_count(a,b), output