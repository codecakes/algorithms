## This is merge
def merge(arr, left_lo, left_hi, right_lo, right_hi):
    # initialize vars
    arr_ln = right_hi - left_lo + 1
    aux = array('i', [0]*(arr_ln))
    left_i = left_lo
    right_j = right_lo
    index = 0

    # print left_i, left_hi, right_j, right_hi
    # print arr[left_i:left_hi+1], arr[right_j:right_hi+1]
    # fill in the aux array with corre
    while left_i <= left_hi and right_j <= right_hi:
        if arr[left_i] <= arr[right_j]:
            aux[index] =  arr[left_i]
            index += 1
            left_i += 1
        else:
            aux[index] = arr[right_j]
            index += 1
            right_j += 1

    # fill in rest with correct order smallest array first
    while left_i<=left_hi:
        aux[index]= arr[left_i]
        left_i += 1
        index += 1
    # then bigger a
    while right_j<= right_hi:
        aux[index]= arr[right_j]
        right_j += 1
        index += 1
    # overwrite the indices in original arr with new sorted array
    for i in xrange(right_hi - left_lo +1):
        arr[i+left_lo] = aux[i]

# This is merge sort
def merge_split(arr, lo, hi):
    if lo<hi:
        # split array in half
        mid = (lo+hi)/2
        merge_split(arr, lo, mid)
        merge_split(arr, mid+1, hi)
        merge(arr, lo, mid, mid+1, hi)
        # print split_c
        return