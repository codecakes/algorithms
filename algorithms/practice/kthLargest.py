"""
In a sorted array of non-unique numbers, print out the kth largest
"""

def kthLarge(arr, N, maxNum, k):
    '''
        arr: sorted Array;
            Takes <O(N) time complexity assuming some ~NlgN sorting has been performed
        N: Len(arr)
        maxNum: max(arr)
        k: kth largest 0..N-1
    '''
    count = N-1
    k -= 1
    if k == 0: return maxNum
    while (k):
        res = arr[count]
        while (res == maxNum):
            count -= 1
            res = arr[count]
        k -= 1
        count -= 1
        maxNum = res
    return res


# A = sorted(range(9))
# print A
# print kthLarge(A, len(A), max(A), 1)