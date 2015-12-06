"use strict";

let mergeArr = {

    compare: function compare (curIndex, prevIndex, arr) {
        /** if second index is less than first
         * <, rather than <= is what makes this comparator stable
         * thus makes the merge stable
         */
        return arr[prevIndex] > arr[curIndex] ? true:false;
    },

    merge: function merge(firstIndex,firstIndexEnd,secondIndex, secondIndexEnd, N, arr, aux) {
        let
            count = 0;
        secondIndexEnd = secondIndexEnd < N? secondIndexEnd: N-1;
        // fill all elements before the firstIndex i.e. things already sorted
        while (count < firstIndex ) {
            aux[count] = arr[count++];
        }
        // console.log('elements already sorted');
        // console.log(aux);

        // compare and order the list
        while ( firstIndex<=firstIndexEnd && secondIndex <= secondIndexEnd) {
            if ( this.compare(firstIndex, secondIndex, arr) ) {
                // console.log("firstIndex is: "+firstIndex+" and element is: "+ arr[firstIndex]);
                aux[count++] = arr[firstIndex++];
            }
            else {
                // console.log("secondPtr is: "+secondIndex+" and element is: "+ arr[secondIndex]);
                aux[count++] = arr[secondIndex++];
            }
        }
        // console.log("after compare sort");
        // console.log(aux);

        // fill the remnants in the list
        while ( firstIndex <= firstIndexEnd ) {
            aux[count++] = arr[firstIndex++];
        }
        while ( secondIndex <= secondIndexEnd ) {
            aux[count++] = arr[secondIndex++];
        }
        while ( count < N ) {
            aux[count] = arr[count++];
        }
        // console.log("after sorting out the remnants");
        // console.log(aux);
    },

    mergeSort: function mergeSort(arr) {
        /** A Bottoms-Up Merge Sort
         * - Divide the List at each Iteration Pass lgN times, increment each time
         * - Each time slice and dice and merge the array elements in 1, 2, 4, 8, 2^(each Iteration Pass) sub-arrays
         *
         * Uses extra memory O(N), NlgN times;
         */
        // console.log("array is:");
        // console.log(arr);
        let
            N = arr.length,
            gap=0,
            hop = 0,
            end=0,
            array=arr,
            aux=[];
        for (let iterPass=0, ln = Math.ceil(Math.log2(N)); iterPass < ln; iterPass++) {
            // Divide the List at each Iteration Pass lgN times, increment each time
            gap = Math.pow(2, iterPass),
            hop=0, end=0;
            while (hop < N ) {
                // Each time slice and dice and merge the array elements in 1, 2, 4, 8, 2^(each Iteration Pass) sub-arrays
                end = hop+gap;
                // console.log(hop,hop+gap-1,end,end+gap-1);
                this.merge(hop,hop+gap-1,end,end+gap-1, N, array, aux);
                array = aux;
                aux = [];
                hop = end+gap;
                }
        }
        return array;
    }
};
// for testing and debugging purpose only
// let
//     mergeFn = Object.create(mergeArr);

// let arr = [6,5,3,2,1,4];
// let arr = ['A1','B3','B2',"A0"];

// console.log(mergeFn.mergeSort(arr));

// arr = [1000,-300,1,0,90,3,50]
// console.log(mergeFn.mergeSort(arr));

// arr = []
// function rangeRand (min, max) {
//     // Generates a random number between min and max excluding max
//     return Math.floor(Math.random() * (max-min)) + min;
// }

// for (let i=0; i<9; i++) {
//     arr.push(rangeRand(-1000,600));
// }
// console.log(arr);
// console.log(mergeFn.mergeSort(arr));