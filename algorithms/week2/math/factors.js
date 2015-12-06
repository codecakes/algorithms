function factorization (num) {
    //factorization
    let
        arr = [],
        count=1,
        a=0,
        root = Math.ceil(Math.sqrt(num));

    while (count < root) {
        // O(sqrt(N))
        a=num/count;
        if (num%count === 0 && a === parseInt(a)) {
            if (a !== count) {
                arr.push(count, a);
            } else {
                arr.push(count);
            }
        }
        count++;
    }
    return arr;
}