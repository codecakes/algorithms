from math import ceil, log

def merge(left, right):
    left_ln = len(left)
    right_ln = len(right)
    aux = []
    left_i = right_j = 0
    while left_i<left_ln and right_j<right_ln:
        num_left = left[left_i]
        num_right = right[right_j]
        if (num_left<num_right):
            aux.append(num_left)
            left_i += 1
        else:
            aux.append(num_right)
            right_j += 1

    index, slice_arr = (left_i, left) if left_i<left_ln else (right_j, right)
    slice_ln = len(slice_arr)
    while index<slice_ln:
        # print index, slice_arr
        aux.append(slice_arr[index])
        index += 1

    return aux

def merge2(left, right):
    left_ln = len(left)
    right_ln = len(right)
    aux = []
    left_i = right_j = 0
    while left_i<left_ln and right_j<right_ln:
        num_left = left[left_i][0]
        num_right = right[right_j][0]
        if (num_left<num_right):
            aux.append(left[left_i])
            left_i += 1
        else:
            aux.append(right[right_j])
            right_j += 1

    index, slice_arr = (left_i, left) if left_i<left_ln else (right_j, right)
    slice_ln = len(slice_arr)
    while index<slice_ln:
        # print index, slice_arr
        aux.append(slice_arr[index])
        index += 1

    return aux

def mergesort(arr, ln):
    '''Recursive top down out of place space intensive merge sort'''
    if ln > 1:
        mid = ln//2
        # slicing and dicing
        left = arr[:mid]
        left = mergesort(left, len(left))
        right = arr[mid:]
        right = mergesort(right, len(right))
        # once its single length array, merge the two
        # print left, right
        return merge(left, right)
    else:
        # print arr
        return arr

def mergesort_iter(arr, ln):
    '''Iterative top down out of place space intensive merge sort'''
    stack = [arr]
    mergeList= []
    while stack:
        arr = stack.pop()
        ln = len(arr)
        if len(mergeList) > 1:
            mergeList.append(merge(mergeList.pop(), mergeList.pop()))
        if ln > 1:
            mid = ln//2
            # slicing and dicing
            left = arr[:mid]
            stack.append(left)
            right = arr[mid:]
            stack.append(right)
            # print left, right
        else:
            # once its single length array, merge the two
            mergeList.append(arr)
    while len(mergeList) > 1:
        mergeList.append(merge(mergeList.pop(), mergeList.pop()))
    return mergeList[0]

def mergesort_iter2(arr, merge_func=merge2):
    '''Iterative top down out of place space intensive merge sort'''
    stack = [arr]
    mergeList= []
    while stack:
        arr = stack.pop()
        ln = len(arr)
        if len(mergeList) > 1:
            mergeList.append(merge_func(mergeList.pop(), mergeList.pop()))
        if ln > 1:
            mid = ln//2
            # slicing and dicing
            right = arr[mid:]
            stack.append(right)
            left = arr[:mid]
            stack.append(left)
            # print left, right
        else:
            # once its single length array, merge the two
            mergeList.append(arr)
    while len(mergeList) > 1:
        mergeList.append(merge_func(mergeList.pop(), mergeList.pop()))
    return mergeList[0]

def mergesortRec2(arr, ln):
    '''Recursive top down out of place space intensive merge sort'''
    if ln > 1:
        mid = ln//2
        # slicing and dicing
        left = arr[:mid]
        left = mergesortRec2(left, len(left))
        right = arr[mid:]
        right = mergesortRec2(right, len(right))
        # once its single length array, merge the two
        # print left, right
        return merge2(left, right)
    else:
        # print arr
        return arr

def mergesort_bottomUp(arr, merge_func = merge):
    aux = []
    gap = 0
    exp = 0
    ln = len(arr)
    levels = ceil(log(ln))
    array = arr
    while gap <= levels:
        exp = 2**gap
        lo = hi = 0
        while lo < ln:
            hi = lo + exp
            # print exp, lo,hi, array[lo:hi]
            aux.extend(merge_func(array[lo:hi], array[hi:hi+exp]))
            lo = hi+exp
        array = aux
        aux = []
        # print array
        gap += 1
    return array

if __name__ == "__main__":
    A = [38, 27, 43, 50, 39]

    print mergesort_bottomUp(A)

    assert mergesort(A, len(A)) == [27, 38, 39, 43, 50]
    assert mergesort_iter(A, len(A)) == [27, 38, 39, 43, 50]

    arr = [[0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [4, 'ij'], [0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [0,  'ij'], [4, 'that'], [3, 'be'],
            [0, 'to'], [1,  'be'], [5,  'question'], [1, 'or'], [2, 'not'], [4, 'is'], [2, 'to'], [4, 'the']]

    for index in xrange(len(arr)//2):
        arr[index][1] = '-'

    # Out of place and Not stable sorting
    # print arr
    # print mergesortRec2(arr, len(arr))
    # print ' '.join([char[1] for char in mergesortRec2(arr, len(arr))])
    # assert mergesortRec2(arr, len(arr)) == "- - - - - to be or not to be - that is the question - - - -"

    # Out of place and Stable sort but uses additional space
    # print mergesort_iter2(arr)
    assert ' '.join([char[1] for char in mergesort_iter2(arr)]) == "- - - - - to be or not to be - that is the question - - - -"

    # Bottom-Up merge sort with efficient sub array memory usage but not Stable Sort
    assert mergesort_bottomUp(arr, merge_func=merge2)
    # print ' '.join([char[1] for char in mergesort_bottomUp(arr, merge_func=merge)])

    # Concluding mergesort_iter2 with merge_func=merge2/merge is Stable out of place sort with additional O(n) space