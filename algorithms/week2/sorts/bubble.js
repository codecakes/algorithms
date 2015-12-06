"use strict";

function compare (curIndex, prevIndex, arr) {
    //if second index is less than first
    if ( arr[prevIndex] > arr[curIndex] ) {
                return true;
    }
    return false;
}

function swap(minIndex, j, arr) {
    let t=0;
    t = arr[minIndex];
    arr[minIndex] = arr[j];
    arr[j] = t;
}

function bubbleSort (arr) {
    let
    ln = arr.length,
    //stop the bubble pass after the iterations where no swaps were performed
    flag=true;

    // #O(N^2)
    for (let k=0; k<ln; k++) {
        if (!flag) {
            return;
        }
        for (let index=0, limit=ln-1-k; index<limit; index++) {
            if ( compare(index + 1, index, arr) ) {
                swap(index, index+1, arr);
                flag = true;
            } else {
                flag = false;
            }
        }
        flag = false || flag;
    }
}