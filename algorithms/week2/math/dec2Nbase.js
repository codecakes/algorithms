function dec2Nbase (num, radix) {
    // supports only till base 2-36
    let arr = [];
    while (num !== 0) {
        arr.unshift((num%radix).toString(radix).toLocaleUpperCase());
        num = parseInt(num/radix);
    }
    return arr.join('');
}

function nbase2Dec (nbaseNum, radix) {
    //no need to use. just use parseInt. Only for academic purpose
    let
        count=nbaseNum.length - 1,
        ln=0,
        sum=0;
    while (count >= 0) {
        sum += (parseInt(nbaseNum[count], radix)) * Math.pow(radix,ln);
        ln++;
        count--;
    }
    return sum;
}