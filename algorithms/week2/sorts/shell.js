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

function hkLen (N) {
    //Using Tokuda, 1992 for Gap sequence-generation
    let hk = 1, res=0, gaps=[];
    while ( res <= N ) {
        res = Math.ceil( (Math.pow(9,hk) - Math.pow(4,hk))/(5*Math.pow(4,hk-1)) );
        if ( !(res < N) ) break;
        gaps.unshift(res);
        hk++;
    }
    return gaps;
}

function shellSort (arr) {
    const
        N = arr.length,
        gaps = hkLen(N);
    let
        index = 0,
        innerPtr=0;
    //for each h-interleaved gap
    for (var gap of gaps) {
        //start from the gap index
        index = gap;
        //while index < total length, keep incrementing
        while (index < N) {
            //start from the index
            innerPtr = index;
            while (innerPtr >= gap && compare(innerPtr, innerPtr-gap, arr) ) {
                //compare the inner index with the index 'gap' steps earlier in the array
                //swap if needed
                swap(innerPtr, innerPtr-gap, arr);
                //decrement back to inner index 'gap' steps earlier
                innerPtr -= gap;
            }
            index++;
        }
    }
}

// for testing and debugging purposes only
// var arr = [4,2,500,-40, -3000, 0, 0, 5, 6, 60, -40];
// shellSort(arr);
// console.log(arr);