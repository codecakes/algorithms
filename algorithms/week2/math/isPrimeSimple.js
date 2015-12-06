function isPrimes(num) {
    //Verify if the Number is a Prime - by an iterative approach ~sqrt(N)
    //Woks Good for numbers below 170141183460469231731687303715884105727 a prime
    if (num <= 1) return false;
    if (num == 2) return true;

    var i = 2, root = Math.ceil(Math.sqrt(num));
    while (i <= root) {
        if ( num%i === 0 ) {
            return false;
        }
        i++;
    }
    return true;
}