"use strict";

function compare (curIndex, otherIndex, arr) {
    //if second index is less than first
    if ( arr[otherIndex] > arr[curIndex] ) {
                return true;
    }
    return false;
}

function swap(minIndex, j, arr) {
    var t;
    t = arr[minIndex];
    arr[minIndex] = arr[j];
    arr[j] = t;
}

function selectionSort (arr) {
    //like bubblesort but bubbles minimum at the begining of array from L-R;
    // in-place sorting because swapping involves accessing indices. array Access time O(1)
    const ln = arr.length;
    let index = 0, j=0, minIndex=0;
    while ( index < ln ) {
        j = index+1;
        minIndex = index;
        //find min once throughout the loop
        while (j < ln) {
            if ( compare(j, minIndex, arr) ) {
                minIndex = j;
            }
            j++;
        }
        //swap after the sweep
        if ( minIndex !== index ) {
            swap(minIndex, index, arr);
        }
        index++;
    }
}

// for testing and debugging purposes only
// var arr = [4,2,500,-40, -3000, 0, 0, 5, 6, 60, -40];
// selectionSort(arr);
// console.log(arr);