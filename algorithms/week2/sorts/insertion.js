"use strict";

function compare (curIndex, prevIndex, arr) {
    //if second index is less than first
    if ( arr[prevIndex] > arr[curIndex] ) {
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

function insertionSort (arr) {
    const ln = arr.length;
    let index = 0, innerPtr=0;
    // O(N^2)
    while ( index < ln ) {
        innerPtr= index;
        while (innerPtr > 0) {
            //Compare each element per iteration
            if ( compare(innerPtr, innerPtr-1, arr) ) {
                //and swap ecah element and previous one per inner iteration
                swap(innerPtr, innerPtr-1, arr);
            }
            innerPtr--;
        }
        index++;
    }
}

// for testing and debugging purposes only
// var arr = [4,2,500,-40, -3000, 0, 0, 5, 6, 60, -40];
// insertionSort(arr);
// console.log(arr);