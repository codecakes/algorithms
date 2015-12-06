"""
Union-Find:
1. Given a set of numbers, Do Random Joins as tuples or sets;
2. Given a set of Unions, Find Connections;

Quick Weighted Union:
- Array arr contains all numbers as indexes, the size of arr is noted;
- Sub Module Get_Root finds the root of the current key. if cur_key root is not set to this root, sets it.
- A merge checks for size of each arr, adds the root of Smaller Tree to Larger Tree. Size of Tree is determined either by:
    - Height
    - Number of Nodes
    - Rank
"""

def find_connection(num1, num2, arr):
    '''Find if connection exists between two nodes'''
    #O(N)
    return ( get_root(num1, arr) == get_root(num2, arr) and get_root(num1, arr) != None )

def get_root(num, arr):
    '''
    Given an array of weighted root indexes arr:
        1. Gets the root of the num in the current tree which its in
        2. returns the root
    '''
    if arr[num] == None: return None
    #O(N)
    while ( num != arr[num] ):
        #set the current key's root if not set
        #set_root(num, arr[num])
        num = arr[num]
    return num


def set_root(num, root, arr):
    '''
        1. Sets the given root of current num in arr if not set
    '''
    #O(1)
    arr[num] = root

def set_all_root(num1_root, num2_root, arr):
    '''
        ~lgN
        Set root of all numbers pointing to the the num @num1_root to the num @ num2_root in arr
    '''
    res = arr
    ln = len(res)/2
    stack = [res[:ln], res[ln:]]
    while stack:
        #lgN
        res = stack.pop()
        if len(res) != 1:
            ln = len(res)/2
            stack.insert(0, res[ln:])
            stack.insert(0, res[:ln])
        elif res[0] == num1_root:
            #O(1)
            set_root(res[0], num2_root, arr)

def get_size(key, arr):
    '''
        Given a size_arr and leaf key, find the size of the tree given
            arr: array of roots and their tree's corresponding size count

        Returns:
            count
    '''
    count = 0
    #O(N)
    while ( key != arr[key] ):
        key = arr[key]
        count += 1
    return count

def get_root_set_size(num, arr, size_arr):
    '''
    same as get_root but with side effect of setting size as well
    '''
    if arr[num] == None: return None
    count = 1
    #O(N)
    while ( num != arr[num] ):
        #set the current key's root if not set
        #set_root(num, arr[num])
        num = arr[num]
        count += 1
    set_size(num, count, size_arr)
    return num

def set_size(root_key, count, size_arr):
    '''
    Evaluate the size of each tree from arr and set it in size_arr
        root_key: Root key of the tree
        count: Number of nodes in a tree
        size_arr: hashmap/dict of roots and their tree's corresponding size count
    '''
    #O(1)
    size_arr[root_key] = count

def find_greatest_element_component(num, arr):
    '''
        Add a method find() to the union-find data type so that find(i) returns
        the largest element in the connected component containing i.
        The operations, union(), connected(), and find() should all take logarithmic time or better.

        For example, if one of the connected components is {1,2,6,9},
        then the find() method should return 9 for each of the four elements in
        the connected components because 9 is larger 1, 2, and 6.
    '''
    maximus = num
    while ( num != arr[num] ):
        num = arr[num]
        if (maximus < num):
            maximus = num
    return maximus

def find_lowest_element_component(num, arr):
    '''
        same as find_greatest_element_component except it finds the minimum element in the Tree component
    '''
    minimus = num
    while ( num != arr[num] ):
        num = arr[num]
        if (minimus > num):
            minimus = num
    return minimus

def qwc(num1, num2, arr, size_arr):
    '''
    Weighted Quick Union with Path Compression
    Given the size_arr sized array and two weighted numbers num1 and num2:
        1. Find their roots.
        2. If same, return
        3. If different:
            - Find size of each root's tree;
            - Cmp for the smaller tree;
            - Point the self reflecting root of smaller tree parent node to larger tree parent node;
        4. return merged tree;

    Params:
        arr: Array of keys in question pointing to its immediate root
        size_arr: hashmap/dict of roots and their tree's corresponding size count
    '''
    #Find if there alrdy exists a connection no need for union
    if find_connection(num1, num2, arr): return None  #O(N)

    #get the root key of the given current key #~lgN - ~(N)
    num1_root = get_root(num1, arr)
    num2_root = get_root(num2, arr)

    #set the current key's root if not set
    #O(1)
    set_root(num1, num1_root, arr)
    set_root(num2, num2_root, arr)

    #Get the size of the current root keys tree - O(1)
    num1_tree_size = size_arr[num1_root]
    num2_tree_size = size_arr[num2_root]

    #set the smaller tree's root to bigger one
    if ( num2_tree_size > num1_tree_size ):
        set_root(num1_root, num2_root, arr)
        set_all_root(num1_root, num2_root, arr)
        set_size(num2_root, size_arr[num2_root]+size_arr[num1_root], size_arr) #size_arr[num2_root] += size_arr[num1_root]
        #set_size( num1_root, size_arr[num2_root], size_arr )  #size_arr[num1_root] = size_arr[num2_root]
    else:
        set_root(num2_root, num1_root, arr)
        set_all_root(num2_root, num1_root, arr)
        set_size(num1_root, size_arr[num1_root]+size_arr[num2_root], size_arr)
        #set_size(num2_root, size_arr[num1_root], size_arr)
    return arr


if __name__ == "__main__":
    #for debugging purposes only
    from random import randint, choice
    seed = 25
    numbers = {randint(0, seed) for _ in xrange(seed)}
    arr = [i for i in xrange(max(numbers))]
    size_arr = {i: get_size(i, arr)+1 for i in arr}

    assert find_connection(1, 2, arr) == False
    assert get_root(1, arr) == 1
    assert get_root(2, arr) == 2
    assert get_root(0, arr) == 0

    print qwc(1,2, arr, size_arr)
    print qwc(3,5, arr, size_arr)
    print qwc(5,2, arr, size_arr)
    assert get_root(2, arr) == 3
    print qwc(10,19, arr, size_arr)
    print qwc(6,2, arr, size_arr)
    print "--"*10
    print qwc(11,20, arr, size_arr)
    print qwc(20,21, arr, size_arr)
    print qwc(16,21, arr, size_arr)
    print qwc(14,23, arr, size_arr)
    print qwc(21,23, arr, size_arr)
    print "--"*10
    print qwc(23,2, arr, size_arr)
    print "--"*10


