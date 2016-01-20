# Enter your code here. Read input from STDIN. Print output to STDOUT

'''
Problem Statement

Bob is a dance teacher and he started dance classes recently. He observes a strange attendance pattern among his students. Initially, there are no students. On day i, a new student starts attending the class. The student stops attending the class, if and only if he has attended the class for i consecutive days. Also, the student resumes attending the class, if and only if he has not attended the class for i consecutive days.

We denote the student who starts coming on day i as student i.
To mark attendance, o denotes present and x denotes absent.

For example, the schedule for student 1 from day 1 is as follows:
oxoxoxoxoxoxoxoxoxox...

The schedule for the student 3 from day 1 is as follows:

xxoooxxxoooxxxoooxxx...
(Student 3 starts attending the class from day 3, and stops attending from day 6, and then starts attending from day 9, and so on. )

The schedule for the student 5 from day 1 is as follows. xxxxoooooxxxxxoooooxxxxx...

Bob wants his students to dance in pairs. However, if the number of students coming on day i is odd, then there will be someone who can't find a partner. So Bob wants to know if the number of students coming on day i is even or odd. We denote the number of students coming on day i as N(i). Please find out whether N(i) is even or odd.

Input format

The first line contains an integer, T, which denotes the number of test cases.
For each test case, there is an integer i

Output Format
For each test case, if N(i) is even, then print even.
If N(i) is odd, then print one line odd.

Constraints
1 <= T <= 100
1 <= i <= 1018

Sample Input

4
1
2
3
4
Sample Output

odd
odd
odd
even
Explanation
The number of students coming on day 1 is 1: only student #1 attends the class. So N(1)=1 and it is odd.
The number of students coming on day 2 is 1: student #2, so n(2)=1 and it is odd.
The number of students coming on day 3 is 3: student #1, student #2, and student #3. So N(3)=3 and it is odd.
The number of students coming on day 4 is 2: student #3 and student #4. So N(4)=2 and it is even.
'''

"""
Scale:

For a given Day, D, how many i's (agents) exist that will be present on that Day D <==> The # of i's | D(D,i) = odd.
How many i's from the R(1-->D) s.t. (D//i)%2 == 1 ??
"""
#present = lambda D,i: False if (((D-(D%i))/i)) %2 == 0 else True
# is same as Qoutient mod 2
present = lambda D,i: False if (D//i) %2 == 0 else True


# def even_odd(D):
#     count = 0
#     # days = range(1, D+1)
#     # stack = [days]
#     # lo = mid = 0
#     # while (stack):
#     #     days = stack.pop()
#     #     ln = len(days)
#     #     if ln > 1:
#     #         mid = (lo+ln)//2
#     #         if lo<mid and mid<=ln:
#     #             stack.append(days[:mid])
#     #             stack.append(days[mid:])
#     #     else:
#     #         day = days[0]
#     #         if present(D, day): count += 1
#     # return 'even' if not count%2 else 'odd'
#     for day in xrange(1, D+1):
#         if present(D, day): count += 1
#     return 'even' if not count%2 else 'odd'

max_day_allowed = 10**18

# t = int(raw_input())

def sqr_root(n):
    # Integer Square Root by Recurring Bisection Method
    x = float(1)
    y = float(n+1)
    lo = 0
    while(abs(y-x) > 1):
        mid = (x+y)//2
        x,y = (mid, y) if mid*mid <= n else (x, mid)
    return x

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


def even_odd(D):
    n = find_invpow(D, 2) %2 if len(str(D)) > 10 else sqr_root(D)%2
    #if its a perfect square its Odd numbers of divisors, else it is even
    return 'odd' if n else 'even'

if __name__ == "__main__":
    import sys
    fname = sys.argv[1]
    ans = sys.argv[2]
    with open(ans) as fans:
        with open(fname) as f:
            t = int(f.readline().strip().strip('\n'))
            assert t==100
            # print "t is %s" %t
            if 1<=t<=100:
                for _ in xrange(t):
                    # D = int(raw_input())
                    D = int(f.readline().strip().strip('\n'))
                    output = (fans.readline().strip().strip('\n'))
                    if 1<= D <= max_day_allowed:
                        #D = int(floor(sqrt(D)))
                        try:
                            assert even_odd(D) == output
                        except AssertionError, e:
                            print "D is %s" %D
                            print even_odd(D)