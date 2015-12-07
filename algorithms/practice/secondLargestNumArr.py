# Find second largest number in a list

from kthLargest import kthLarge

def secondLarge(A, arrLen):
    if (2 <= arrLen <= 10):
        #O(NlgN)
        A.sort()
        #finding max- O(1)
        maxNum = A[-1]
        #omission of max - O(N)
        # res=A.pop()
        # while (res == maxNum):
        #     res = A.pop()
        return kthLarge(A, arrLen, maxNum, 2)