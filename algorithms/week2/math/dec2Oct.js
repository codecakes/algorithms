function dec2Oct (num) {
    let arr = [];
    while (num !== 0) {
        arr.unshift((num%8).toString(8).toLocaleUpperCase());
        num = parseInt(num/8);
    }
    return arr.join('');
}

function Oct2Dec (hexNum) {
    //no need to use. just use parseInt. Only for academic purpose
    let
        count=hexNum.length - 1,
        ln=0,
        sum=0;
    while (count >= 0) {
        sum += (parseInt(hexNum[count], 8)) * Math.pow(8,ln);
        ln++;
        count--;
    }
    return sum;
}