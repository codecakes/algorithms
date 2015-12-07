"""
In a sorted array of non-unique numbers, print out the kth smallest
"""

def kthSmall(arr, N, minNum, k):
    '''
        arr: sorted Array;
            Takes <O(N) time complexity assuming some ~NlgN sorting has been performed
        N: Len(arr)
        minNum: min(arr)
        k: kth largest 0..N-1
    '''
    count = 0
    k -= 1
    if k == 0: return minNum
    #at each kth step decrement to go to hunting for next lower number
    while (k):
        res = arr[count]
        while (res == minNum):
            count -= 1
            res = arr[count]
        k -= 1
        count -= 1
        minNum = res
    return res


# A = sorted(range(9))
# print A
# print kthSmall(A, len(A), min(A), 1)