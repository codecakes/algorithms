function dec2Hex (num) {
    let arr = [];
    while (num !== 0) {
        arr.unshift((num%16).toString(16).toLocaleUpperCase());
        num = parseInt(num/16);
    }
    return arr.join('');
}

function hex2Dec (hexNum) {
    //no need to use. just use parseInt. Only for academic purpose
    let
        count=hexNum.length - 1,
        ln=0,
        sum=0;
    while (count >= 0) {
        sum += (parseInt(hexNum[count], 16)) * Math.pow(16,ln);
        ln++;
        count--;
    }
    return sum;
}