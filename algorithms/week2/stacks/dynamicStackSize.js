/**
 * Dynamic version of stackLinkedList except keeps size dynamic.
 *
 * Linked List like implementation of Stack LIFO operations:
 *  - Node: attr
 *      - ItemVal
 *      - next()
 *  - Push
 *  - Pop
 *  - IsEmpty
 *  - IsFull
 *
 * With dynamic resized LinkedList Stacks, one doesn't need to worry about
 * a contingent array block Accessing since Only the Topmost item is needed.
 *
 * Every LinkedList Node refers to the next one.
 *
 * Size keeps a check of how much to push and pop safely.
 *
 * A Stack of size 0 will never push or pop naturally so choose > 0
 *
 * Flipside is linked references are not in a continguous memory block so retrieving can take sometime.
 * Arrays waste less space.
 */

"use strict";
let stackModule = (function () {

let
    createNode = function createNode (val) {
        //Single Unit Node object; Returns a new Node Object
        let Node = {
          init: function init(val) {
              this.val =val;
              //this should always point to the createNode Object;
              this.next=undefined;
          }
        },
        initNode = Object.create(Node);

        initNode.init(val);
        return initNode;
    },
    stackLL = function stackLL (size) {
        //Returns a New Stack Object. First declare a definite size N
        let
            stack = {
                init: function init (size) {
                    this.size = size;
                    this.sizeCtr = 0;
                    this.firstNode = undefined;
                    this.nextNode = undefined;
                    this._old = undefined;
                },
                push: function push(item) {
                    if ( !( this.sizeCtr+1 > this.size ) ) {
                        //iff sizeCtr does not exceed stack size
                        this._old = this.firstNode;
                        this.firstNode = createNode(item);
                        this.firstNode.next = this._old;
                        this.nextNode = this.firstNode.next;
                        this.sizeCtr++;

                        //now check if table doubling is needed
                        this._tableDouble();
                    }
                },
                pop: function pop() {
                    if ( this.sizeCtr > 0 ) {
                        this._old = this.firstNode;
                        this.firstNode = this.firstNode.next;
                        this.nextNode = this.firstNode.next;
                        this.sizeCtr--;

                        //now check if table halving is needed
                        this._tableHalve();
                    }
                },
                isEmpty: function isEmpty() {
                    return this.sizeCtr === 0;
                },
                isFull: function isFull() {
                    return this.sizeCtr === this.size;
                },
                _tableDouble: function _tableDouble () {
                    //doubling efficient only with a condition like following
                    //to allow rare operation of this function
                    if ( this.isFull() ) {
                        this.size *= 2;
                    }
                },
                _tableHalve: function _tableHalve() {
                    //half efficient only with a condition like following
                    //to allow rare operation of this function
                    if (this.sizeCtr <= this.size/4) {
                        this.size /= 4;
                    }
                },
                iter: function* iter () {
                    let iterNext = this.firstNode;
                    while ( typeof iterNext !== "undefined" ) {
                        yield iterNext;
                        iterNext = iterNext.next;
                    }
                }
            },
        newStackObj = Object.create(stack);

        newStackObj.init(size);
        return newStackObj;
    };
return stackLL;
})();

let whichPlat = function () {
function isNode(){try{return this===window;}catch(e){return false;}}
return isNode()?window:global;
};

whichPlat()['stack'] = stackModule;

// only for debugging purposes
// var newStack = stackModule(50),
// log = console.log;

// log(newStack);

// newStack.push(100);
// log(newStack);

// newStack.push(200);
// log(newStack);

// newStack.push(300);
// log(newStack);

// var gen = newStack.iter();
// for (let each of newStack.iter()) {
//     log(each);
// }
//is same as
// log(gen.next().value);
// log(gen.next().value);
// log(gen.next().value);