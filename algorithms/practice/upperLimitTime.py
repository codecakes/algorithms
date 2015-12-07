#!/bin/python


"""
Problem Statement

The professor is conducting a course on Discrete Mathematics to a class of N students. He is angry at the lack of their discipline, and he decides to cancel class if there are fewer than K students present after the class starts.

Given the arrival time of each student, your task is to find out if the class gets cancelled or not.

Input Format

The first line of input contains T, the number of test cases. Each test case contains two lines.
The first line of each test case contains two space-separated integers, N and K.
The next line contains N space-separated integers, a1,a2,…,aN, representing the arrival time of each student.

If the arrival time of a given student is a non-positive integer (ai≤0), then the student enters before the class starts. If the arrival time of a given student is a positive integer (ai>0), the student enters after the class has started.

Output Format

For each test case, print "YES" (without quotes) if the class gets cancelled. Otherwise, print "NO" (without quotes).

Constraints

1≤T≤10
1≤N≤1000
1≤K≤N
−100≤ai≤100,where i∈[1,N]
Note
If a student enters the class exactly when it starts (ai=0), the student is considered to have entered before the class has started.

Sample Input

2
4 3
-1 -3 4 2
4 2
0 -1 2 1
Sample Output

YES
NO

Explanation

For the first test case, K=3. The professor wants at least 3 students to be in class, but there are only 2 who have arrived on time (−3 and −1). Hence, the class gets cancelled.

For the second test case, K=2. The professor wants at least 2 students to be in class, and there are 2 who have arrived on time (0 and −1). Hence, the class does not get cancelled.
"""

t = int(raw_input().strip())

time_slots = []
count = 0

#O(N)
if 1<=t<=10:
    for a0 in xrange(t):
        n,k = map(int, raw_input().strip().split(' '))

        if (1<=n<=1000) and (1<=k<=n):
            slots= [n,k]
            slots.append([int(ai) for ai in raw_input().strip().split(' ') if -100<=int(ai)<=100])
            time_slots.append(slots)

    '''#O(max(N)lgt)
    #Faster, but out of order
    stack = []
    stack.append(time_slots)
    while stack:
        lst = stack.pop()
        ln = len(lst)
        # divide
        if ln > 1:
            left, right = lst[:ln/2], lst[ln/2:]
            stack.insert(0, left)
            stack.insert(0, right)
        else:
            # conquer
            N, K, time_list = lst[0]
            for each_time in time_list:
                if each_time <= 0: count += 1
            if count >= K:
                print 'NO'
            else:
                print 'YES'
            count = 0'''
    #O(N*t)
    for N, K, time_list in time_slots:
        for each_time in time_list:
            if each_time <= 0: count += 1
        if count >= K:
            print 'NO'
        else:
            print 'YES'
        count = 0