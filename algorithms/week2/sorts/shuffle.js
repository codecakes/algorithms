function swap(minIndex, j, arr) {
    var t;
    t = arr[minIndex];
    arr[minIndex] = arr[j];
    arr[j] = t;
}

function rangeRand (min, max) {
    // Generates a random number between min and max excluding max
    return Math.floor(Math.random() * (max-min)) + min;
}

function shuffle (arr) {
    // in-place Shuffle
    for (let index=0, ln = arr.length; index<ln; index++) {
        // ~O(N)
        //to be truly uniformly random, min and max are least and present greatest value
        swap(rangeRand(0, index), index, arr);
    }
    return arr;
}