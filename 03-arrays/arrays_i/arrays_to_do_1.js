// PUSH FRONT

function pushFront(arr, num) {
    for (idx = arr.length; idx >= 0; idx--) {
        arr[idx] = arr[idx-1];
    }
    arr[0] = num;
    return arr;
}

// console.log(pushFront([5,7,2,3], 8));
// console.log(pushFront([99], 7));

// =====

// POP FRONT

function popFront(arr) {
    for (idx = 0; idx < arr.length-1; idx++) {
        arr[idx] = arr[idx+1];
    }
    arr.pop();
    return arr;
}

// console.log(popFront([0,5,10,15]));
// console.log(popFront([4,5,7,9]));

// =====

// INSERT AT

function insertAt(arr, idx, val) {
    for (num = arr.length; num >= 0; num--) {
        arr[num] = arr[num-1]
        if (num == idx) {
            arr[num] = val;
            return arr;
        }
    }
}

// console.log(insertAt([100,200,5], 2, 311));
// console.log(insertAt([9,33,7], 1, 42));