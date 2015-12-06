function primeFactorization (N) {
    //factorization using only primes
    let
        arr = [],
        count=2,
        a=0,
        b=N,
        root = Math.ceil(Math.sqrt(N));

    while (count < root) {
        // O(sqrt(N))
        a= b;
        b = b/count;
        while (parseInt(b) !== 0 && parseInt(b) === b) {
            arr.push(count);
            a=b;
            b /= count;
        }
        b=a;
        count++;
    }
    if (a>1) {
        arr.push(a);
    }
    return arr;
}