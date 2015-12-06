/**
 * Shuffling a given Array reduces the chances of O(N^2)
 * by making sure the balance after partitioning creates evenly parted pivots
 * i.e. the split partitioned arrays will also be randomly balanced;
 * Shuffling will take Linear Time ~ O(N)
 *
 * Note: One could do stable quicksort with an Additional Array appraoch.
 * That would have more space cost and computational cost.
 */
// Swaps two items in an array, changing the original array

var swap = function(array, firstIndex, secondIndex) {
    var temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;
};

// This function partitions given array and returns
//  the index of the pivot.
var partition = function(array, p, r) {
    /* incorporate Dijkstra 3-way Partiitoning for duplicate pivot keys */
    var pivotIndex =parseInt((p+r)/2),
        pivot=0;
    swap(array, pivotIndex, r);
    pivotIndex = r;
    pivot=array[pivotIndex];
    // Compare array[j] with array[r], for j = p, p+1,...r-1
    // maintaining that:
    //  array[p..q-1] are values known to be <= to array[r]
    //  array[q..j-1] are values known to be > array[r]
    //  array[j..r-1] haven't been compared with array[r]
    // If array[j] > array[r], just increment j.
    // If array[j] <= array[r], swap array[j] with array[q],
    //   increment q, and increment j.
    // Once all elements in array[p..r-1]
    //  have been compared with array[r],
    //  swap array[r] with array[q], and return q.
    for (var lo=p, eq=p, hi=p; hi < r ;hi++) {
        // at this point hi ptr !== pivotIndex
        if (array[eq] == pivot) {
            eq++;
        }
        if ( array[hi] < pivot && hi !== pivotIndex ) {
            swap(array, hi, lo);
            lo++;
            eq++;
        }
    }
    swap(array, lo, pivotIndex);
    //the pivot goes to index @ lo and number @lo goes to index @ pivotIndex
    return lo;
};

//in-place unstable O(NlgN) Avg-case Comparison Sort - Iterative Version
var quickSort = function(array, p, r) {
    var stack = [[p,r]], pop;
    while (stack.length > 0) {
        // console.log("stack is "+ stack);
        pop = stack.pop();
        p = pop[0], r = pop[1];
        if (p < r) {
            // divide using Linear-partitioning
            var pivotIndex = partition(array, p, r);
            // conquer - is in the stack
            stack.unshift([p, pivotIndex-1]);
            stack.unshift([pivotIndex+1, r]);
        }
    }
    return;
};

//find the kth smallest element without the Brute Force Sort All, find kth
//just do it by comparing the returned pivot index
var quickSelectIter = function quickSelectIter(array, startIndex, endIndex, k) {
    var
        stack = [[startIndex,endIndex]],
        pop, pivotIndex=0;
    while (stack.length > 0) {
        pop = stack.pop();
        startIndex = pop[0], endIndex = pop[1];
        if (startIndex <= endIndex) {
            // divide using Linear-partitioning
            pivotIndex = partition(array, startIndex, endIndex);
            // console.log("pivotIndex is " + pivotIndex + " with pivot element " + array[pivotIndex]);
            // console.log("array is " + array);
            if ( pivotIndex === k ) return array[pivotIndex];

            if (pivotIndex > k) {
                stack.unshift([startIndex, pivotIndex-1]);
            } else if (pivotIndex < k) {
                stack.unshift([pivotIndex+1, endIndex]);
            }
        }
    }
};

//in-place unstable O(NlgN) Avg-case Comparison Sort - Recursive Version
var quickSortRec = function(array, p, r) {
    if (p < r) {
        // divide
        var pivotIndex = partition(array, p, r);
        // conquer
        quickSortRec(array, p, pivotIndex-1);
        quickSortRec(array, pivotIndex+1, r);
    }
    return;
};

// for testing and debugging use only
var array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6];
quickSort(array, 0, array.length-1);
console.log("sorted array is: ", array);
array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6];
quickSortRec(array, 0, array.length-1);
console.log("sorted array is: ", array);
var array = [2,3,6,6,5];
console.log(quickSelectIter(array, 0, array.length-1, 3));
array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6];
console.log(quickSelectIter(array, 0, array.length-1, 4));
array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6];
console.log(quickSelectIter(array, 0, array.length-1, 0));
array = [9, 9, 9, 11, 12, 2, 14, 3, 10, 6];
quickSort(array, 0, array.length-1);
console.log(array);