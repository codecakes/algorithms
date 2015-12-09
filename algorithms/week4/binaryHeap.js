
/**
 * Binary Heap
 */

"use strict";

var
    div = function div(num, den) {
        return Math.floor(num/den);
    },
    _attachNodes= function _attachNodes(childNode, parentNode) {
        childNode.parent = parentNode;
        if ( childNode.key%2 === 0 ) {
            parentNode.leftChild= childNode;
        } else {
            parentNode.rightChild = childNode;
        }
    },
    _delNodesRelation= function _delNodesRelation(Node) {
        // remove relation with parent
        if ( Node.parent.leftChild === Node ) { Node.parent.leftChild === undefined; }
        else if ( Node.parent.rightChild === Node ) { Node.parent.rightChild === undefined; }
        Node.parent = undefined;

        // remove relation with children
        if ( !!Node.leftChild ) {
            Node.leftChild.parent = undefined;
            Node.leftChild === undefined;
        }
        if ( !!Node.rightChild ) {
            Node.rightChild.parent = undefined;
            Node.rightChild === undefined;
        }
    },
    heapSwap = function heapSwap (array, Node1, Node2) {
        // Swaps two items in an array, keeping their respective relations
        var
            node1Val = Node1.val,
            node2Val = Node2.val;

        Node2.val = node1Val;
        Node1.val = node2Val;
    },

    hasChild = function hasChild(Node) {
        return !!Node.leftChild || !!Node.rightChild;
    },

    lowerChild = function lowerChild (Node) {
        // for minHeap
        return Node.leftChild.val < Node.rightChild.val ? Node.leftChild:Node.rightChild;
    },

    swimUpComparator = function swimUpComparator (Node) {
        // compare with parent if it's greater than the node
        console.log("in swim comparator. node is");
        console.log(Node);
        return !!Node.parent? (Node.parent.val > Node.val): false;
    },
    sinkDownComparator = function sinkDownComparator(Node, greaterNode) {
        // compare with children if they're lesser than the node
        return !!greaterNode? (Node.val > greaterNode.val): false;
    },

    createNode = function createNode(val, key) {
        // Each Node has 2 children and a parent. parent maybe null if its itself a parent node;
        var Node = {
            init: function init (val) {
                this.val = val;
                this.key = key;
                this.parent = undefined;
                this.leftChild=undefined;
                this.rightChild = undefined;
            },
        },
        initNode = Object.create(Node);
        initNode.init(val);
        return initNode;
    },

    nodeLeftPos = function nodeLeftPos (index) {
        // node count starts from 0; index is key or position in array;
        return 2*(index);

    },
    nodeRightPos = function nodeRightPos (index) {
        // node count starts from 0; index is key or position in array;
        return (2*index)+1;

    },

    nodeParent = function nodeParent(index) {
        return div( index,2 );
    },

    // An array based Min Binary Heap => Maximum values at top
    minBinaryHeap = {
    // Initialize a heap
    init: function init() {
        this._arr = [null];
        this._insertPos = 1;
    },
    isEmpty: function isEmpty() {
        return (this._insertPos-1)===0;
    },
    swimUp: function swimUp(key) {
        // O(lgN)
        var tempNode = this._arr[key];
        console.log("In swimUp. key is "+key+" node is ");
        console.log(tempNode);
        while ( swimUpComparator(tempNode) ) {
            heapSwap(this._arr, tempNode, tempNode.parent);
            key = div(key,2);
            tempNode = this._arr[key];
        }
    },
    sinkDown: function sinkDown (key) {
        // O(lgN)
        var
            tempNode = this._arr[key],
            // greaterNode = greaterChild(tempNode);
            lowerNode = lowerChild(tempNode);


        while ( sinkDownComparator(tempNode, lowerNode) && !!lowerNode ) {
            heapSwap(this._arr, tempNode, lowerNode);
            key = tempNode.key;
            tempNode = this._arr[key],
            lowerNode = lowerChild(tempNode);
        }
    },
    // insert in a heap
    insert: function insert (val) {
        // insert
        var newNode = createNode(val, this._insertPos);

        //attach relationships
        this._insertPos = this._arr.push(newNode);
        console.log("insertPos is at "+this._insertPos+" and node Parent pos is: " + nodeParent(this._insertPos-1));
        console.log("New Node");
        console.log(newNode);
        if ( this._insertPos-2 > 0 ) {
            console.log("New Node Parent");
            var newNodeParent = this._arr[nodeParent(this._insertPos-1)];
            console.log(newNodeParent);
            _attachNodes(newNode, newNodeParent);
        }
        // compare and swim  if needed
        this.swimUp(this._insertPos-1);
    },
    _delLastLeaf: function delLastLeaf() {
        // remove it
        _delNodesRelation(this._arr.pop());
        //decerement the insert Position
        this._insertPos -= 1;
    },
    delMin: function delMin() {
        if ( !this.isEmpty() ) {
            // delete the root Minimum Node
            // get last node which is the Max Node in Min Binary Heap at root - O(lgN)
            heapSwap(this._arr, this._arr[1], this._arr[this._insertPos-1]);
            // remove the last leaf - O(1)
            this._delLastLeaf();
            //rebalance the heap by sinking Down from root Index, 1. - O(lgN)
            this.sinkDown(1);
        }
    },
    minHeap: function minHeap() {
        // return minimum of minHeap - O(1)
        return this._arr[1].val;
    },
    seek: function seek (key) {
        // O(1)
        return key<this._insertPos?this._arr[key]:undefined;
    },
    print: function print(log) {
        log(this._arr);
    }
};

// for debugging and testing only
// var log = console.log;

// var dummy = function dummy() {
//     // body...
//     return;
// };

// console.log = (function (status) {
//     if (status) return log;
//     else return dummy;
// })(false);

// var heap = Object.create(minBinaryHeap);
// heap.init();
// heap.insert(100);
// heap.insert(-1000);
// heap.insert(-2000);
// heap.insert(20000);
// heap.insert(780);
// heap.insert(2340);
// heap.print(log);
// console.assert(heap.minHeap()==-2000, "Should equal -2000");
// log("------------------------");
// heap.delMin();
// heap.print(log);
// console.assert(heap.minHeap()==-1000, "Should equal 1000");