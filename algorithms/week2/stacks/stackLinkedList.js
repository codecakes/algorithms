/**
 * Linked List like implementation of Stack LIFO operations:
 *  - Node: attr
 *      - ItemVal
 *      - next()
 *  - Push
 *  - Pop
 *  - IsEmpty
 *  - IsFull
 */

"use strict";

const
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
        //Returns a New Stack Object
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
                    }
                },
                pop: function pop() {
                    if ( this.sizeCtr > 0 ) {
                        this._old = this.firstNode;
                        this.firstNode = this.firstNode.next;
                        this.nextNode = this.firstNode.next;
                        this.sizeCtr--;
                    }
                },
                isEmpty: function isEmpty() {
                    return this.sizeCtr === 0;
                },
                isFull: function isFull() {
                    return this.sizeCtr === this.size;
                }
            },
        newStackObj = Object.create(stack);

        newStackObj.init(size);
        return newStackObj;
    };

/**
var s = stackLL(50),
log = console.log;

log(s);
s.pop();
s.push(1);
log(s);
s.push(12);
log(s);
s.pop();
log(s);
*/
