
"use strict";

function compute(a,b,sym) {
    let res=0;
    switch (sym) {
        case '*':
            res= a*b;
            break;
        case '%':
            res= a%b;
            break;
        case '/':
            res= a/b;
            break;
        case '+':
            res= a+b;
            break;
        case '-':
            res= a-b;
            break;
        default:
            break;
    }
    return res;
}

function isNum (x) {
    let res = parseInt(x);
    return !isNaN(res) && typeof res === "number";
}

function computeBod (str) {
    /**
     * - Left Paran: Ignore
     * - Number: put on Value Stack
     * - Operator: Put on Operator Stack
     * - Right Paran: Shift first two top stack values and one Operator value and compute them. Unshift the value back on Number stack.
     *
     * This algorithm takes into account long strings of numbers and doesn't end until it encounters an operator or a Right ending bracket
     */
    const lnStr = str.length, op = ['*','%','/','+','-'];
    let index = 0, a=0,b=0, val=0, number ='', sym, numStack = [], opStack = [];

    while ( index < lnStr ) {
        val = parseInt(str[index]);
        sym = str[index];
        // console.log("str[index] is: " + sym + " val is: "+val);
        if ( isNaN(val) && op.indexOf(sym) > -1 ) {
             //if the val is an operator
             opStack.unshift(sym);
             //check if nunmber is not empty
             if (number !== '') {
                 numStack.unshift(parseInt(number));
                 number = '';
             }
         }
         else if ( isNaN(val) && sym === ')' ) {
             //if closing bracket
             //check if nunmber is not empty
             if (number !== '') {
                 numStack.unshift(parseInt(number));
                 number = '';
             }
             b = numStack.shift();
             a = numStack.shift();
             numStack.unshift( compute(a,b,opStack.shift()) );
         }
         else if ( isNum(sym) ) {
            //if its a number
            //  keep adding the number till it's terminated by a ')' or Operator
            number += sym;
         }
        //  console.log("opStack is:");
        //  console.log(opStack);
        //  console.log("numStack is:");
        //  console.log(numStack);
         index++;
     }
     return numStack.shift();
}

// for debugging and testing purposes only
// console.log( computeBod('(2+((4*5)%(50-6)))') );
// console.log( computeBod('(2+((4*5)%((90*1800) + (50-6))))') );