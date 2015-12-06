function dec2Bin (num) {
    let arr = [];
    while (num !== 0) {
        arr.unshift((num%2).toString());
        num = parseInt(num/2);
    }
    return arr.join('');
}

function bin2Dec (binNum) {
    //no need to use. just use parseInt. Only for academic purpose
    let
        count=binNum.length - 1,
        ln=0,
        sum=0;
    while (count >= 0) {
        sum += (parseInt(binNum[count], 2)) * Math.pow(2,ln);
        ln++;
        count--;
    }
    return sum;
}