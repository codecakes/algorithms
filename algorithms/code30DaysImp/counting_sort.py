T = int(raw_input())

arr = []
for _ in xrange(T):
    arr.append(raw_input().strip('\n').split())

# x = 100


def counting_sort(arr, r):
    '''
    @params:
        - arr: Unsorted Array
        - r: the Range r={min, max} from 0..to r-1
    '''
    n = len(arr)
    #initialize count array from 0 to r inclusive
    count_arr = [0] * r
    aux = [0] * n

    # count frequency
    for num in arr:
        count_arr[num] += 1
    # print count_arr

    # successive accumulative sum per index
    # used to place the key value at right position
    for index in xrange(1,r):
        # print index, index-1
        # print "="*10
        count_arr[index] = count_arr[index-1] + count_arr[index]
    # print ' '.join(map(str, count_arr))

    # place the right key at right position
    for index in xrange(n-1, -1, -1):
        # print index
        aux[count_arr[arr[index]] - 1] = int(arr[index])
        count_arr[arr[index]] -= 1

    # print ' '.join(map(str, aux))
    return aux