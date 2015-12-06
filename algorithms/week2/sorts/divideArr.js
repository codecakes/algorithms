function divide (arr) {
    var
        ln = 0,
        array = arr,
        level = 2*Math.ceil(Math.log2(array.length)),
        left, right,
        len=0,
        stack=[];

    stack.push(arr);

    // >= O(lgN)
    while (level) {
        // this is ~O(lg N)
        array = stack.pop();
        // this takes ~O(N), ~ N/2, ~ N/2^k
        ln = array.length;
        if (ln > 1) {
            len = parseInt(ln/2);
            // these take ~O(N/2)
            left = array.slice(0, len);
            right = array.slice(len);
            // console.log("left is");
            // console.log(left);
            // console.log("right is");
            // console.log(right);
            stack.unshift(left, right);
        } else {
            stack.unshift(array);
        }
        level--;
        // console.log("stack is");
        // console.log(stack);
    }

    return stack;
}