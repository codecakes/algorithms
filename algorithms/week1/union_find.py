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

def get_size(key, arr):
    '''
        Given a size_arr and leaf key, find the size of the tree given 
            arr: hashmap/dict of roots and their tree's corresponding size count

        Returns:
            count
    '''
    count = 0
    #O(N)
    while ( key != arr[key] ):
        key = arr[key]
        count += 1
    return count

def set_size(root_key, count, size_arr):
    '''
    Evaluate the size of each tree from arr and set it in size_arr
        root_key: Root key of the tree
        count: Number of nodes in a tree
        size_arr: hashmap/dict of roots and their tree's corresponding size count
    '''
    #O(1)
    size_arr[root_key] = count

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

    #get the root key of the given current key #O(N)
    num1_index = get_root(num1, arr)
    num2_index = get_root(num2, arr)

    #set the current key's root if not set
    #O(1)
    set_root(num1, num1_index, arr)
    set_root(num2, num2_index, arr)

    #Get the size of the current root keys tree - O(1)
    num1_tree_size = size_arr[num1_index]
    num2_tree_size = size_arr[num2_index]

    #set the smaller tree's root to bigger one
    if (num1_tree_size < num2_tree_size):
        set_root(num1_index, num2_index, arr)
        set_size(num2_index, size_arr[num2_index]+size_arr[num1_index], size_arr) #size_arr[num2_index] += size_arr[num1_index]
        set_size( num1_index, size_arr[num2_index], size_arr )  #size_arr[num1_index] = size_arr[num2_index]
        
    else:
        set_root(num2_index, num1_index, arr)
        size_arr[num1_index] += size_arr[num2_index]
        size_arr[num2_index] = size_arr[num1_index]

    return arr


if __name__ == "__main__":
    #for debugging purposes only
    from random import randint, choice
    seed = 25
    numbers = {randint(0, seed) for _ in xrange(seed)}
    arr = [i for i in xrange(max(numbers))]
    size_arr = {i: get_size(i, arr)+1 for i in arr}

    #print find_connection(1, 2, arr)
    #print get_root(1, arr)
    #print get_root(2, arr)
    #print size_arr

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

    #rand = list({choice(arr) for i in arr})
    #numbers = zip(rand[::2], rand[1::2])
    #print numbers

    #for edge in numbers:
    #    print qwc(edge[0], edge[1], arr, size_arr)


