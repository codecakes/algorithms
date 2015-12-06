function gcd(a,b) {
    let temp=a,rem=b;
    rem = b;
    while (rem !== 0) {
        rem = a%b;
        a=b;
        b=rem;
    }
    return a;
}