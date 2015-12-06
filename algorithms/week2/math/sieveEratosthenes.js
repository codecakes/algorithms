function sieveErastos(num) {
    let
        arr = [],
        root = Math.ceil(Math.sqrt(num));

    for (let count=0; count <=num; count++) {
        arr[count] = 1;
    }
    arr[0] = 0;
    arr[1] = 0;

    // ~(sqrt(N) lglg(N))
    for (let count=2; count <= root; count++) {
        // O(root(N))
        for (let p=2; p*count <= num; p++) {
            // O(lglg(N))
            arr[p*count] = 0;
        }
    }
    return arr;
}