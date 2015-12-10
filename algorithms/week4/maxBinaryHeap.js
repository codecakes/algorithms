
/**
 * Binary Heap
 */

"use strict";

var
    div = function div(num, den) {
        return Math.floor(num/den);
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

    // _attachNodes= function _attachNodes(childNode, parentNode) {
    //     // attach child node to parent and parent to child node at correct limb, Left or Right
    //     childNode.parent = parentNode;
    //     if ( childNode.key%2 === 0 ) {
    //         parentNode.leftChild= childNode;
    //     } else {
    //         parentNode.rightChild = childNode;
    //     }
    // },

    // _delNodesRelation= function _delNodesRelation(Node) {
    //     // remove relation with parent
    //     if ( Node.parent.leftChild === Node ) { Node.parent.leftChild = undefined; }
    //     else if ( Node.parent.rightChild === Node ) { Node.parent.rightChild = undefined; }
    //     Node.parent = undefined;

    //     // remove relation with children
    //     if ( !!Node.leftChild ) {
    //         Node.leftChild.parent = undefined;
    //         Node.leftChild = undefined;
    //     }
    //     if ( !!Node.rightChild ) {
    //         Node.rightChild.parent = undefined;
    //         Node.rightChild = undefined;
    //     }
    // },

    heapSwap = function heapSwap (array, Node1Key, Node2Key) {
        // Swaps two items in an array, keeping their respective relations
        var
            node1Val = array[Node1Key];

        array[Node1Key] = array[Node2Key];
        array[Node2Key] = node1Val;
    },

    // hasChild = function hasChild(Node) {
    //     // Does the Node have children?
    //     return !!Node.leftChild || !!Node.rightChild;
    // },

    swimUpComparator = function swimUpComparator (arr, NodeKey) {
        // compare with parent if it's greater than the node
        console.log("in swim comparator. node is");
        console.log(NodeKey);
        var
            parentNode = arr[nodeParent(NodeKey)],
            childNode = arr[NodeKey];

        return !!parentNode? (parentNode < childNode): false;
    },

    greaterChild = function greaterChild (arr, NodeKey, childKeyLimit) {
        // for maxHeap - see which child node is greater
        var
            rightNodeKey = nodeRightPos(NodeKey),
            leftNodeKey = nodeLeftPos(NodeKey),
            rightNode = arr[rightNodeKey],
            leftNode = arr[leftNodeKey];

        if ( childKeyLimit === rightNodeKey ) {
            rightNode = undefined;
        }
        else if ( childKeyLimit === leftNodeKey ) {
            leftNode = undefined;
        }

        if ( !!rightNode && !!leftNode ) {
            return rightNode > leftNode ? rightNodeKey:leftNodeKey;
        }
        else if ( !rightNode ) {
            return leftNodeKey;
        }
        else {
            return rightNodeKey;
        }
    },

    sinkDownComparator = function sinkDownComparator(arr, parentKey, greaterChildKey) {
        // compare with children if they're lesser than the node
        var
            greaterChild = arr[greaterChildKey],
            parentNode = arr[parentKey];

        return !!greaterChild? (parentNode < greaterChild): false;
    },

    // createNode = function createNode(val, key) {
    //     // Each Node has 2 children and a parent. parent maybe null if its itself a parent node;
    //     var Node = {
    //         init: function init (val) {
    //             this.val = val;
    //             this.key = key;
    //             this.parent = undefined;
    //             this.leftChild=undefined;
    //             this.rightChild = undefined;
    //         },
    //     },
    //     initNode = Object.create(Node);
    //     initNode.init(val);
    //     return initNode;
    // },

    // An array based Min Binary Heap => Maximum values at top
    maxBinaryHeap = {
    // Initialize a heap
    init: function init() {
        this._arr = [null];
        this._insertPos = 1;
    },
    isEmpty: function isEmpty() {
        return (this._insertPos-1)===0;
    },
    swimUp: function swimUp(key) {
        // O(lgN) SwimUp Greater Child Node after each insertion
        var tempNode = this._arr[key];
        console.log("In swimUp. key is "+key+" node is ");
        console.log(tempNode);
        while ( swimUpComparator(this._arr, key) ) {
            heapSwap(this._arr, key, nodeParent(key));
            key = div(key,2);
            tempNode = this._arr[key];
        }
    },
    sinkDown: function sinkDown (key, childKeyLimit) {
        // O(lgN) Sink Down from top to bottom if Invariant not met at top Node
        var
            tempNode = this._arr[key],
            greaterNodeKey = greaterChild(this._arr, key, childKeyLimit);


        while ( sinkDownComparator(this._arr, key, greaterNodeKey) && !!this._arr[greaterNodeKey]) {
            if (!!childKeyLimit) {
                if ( !(greaterNodeKey < childKeyLimit) ) break;
            }
            heapSwap(this._arr, key, greaterNodeKey);
            // key = tempNode.key;
            key = greaterNodeKey;
            tempNode = this._arr[key],
            greaterNodeKey = greaterChild(this._arr, key, childKeyLimit);
        }
    },
    // insert in a heap
    insert: function insert (val) {
        // insert
        // var newNode = createNode(val, this._insertPos);

        //attach relationships
        this._insertPos = this._arr.push(val);
        console.log("insertPos is at "+this._insertPos+" and node Parent pos is: " + nodeParent(this._insertPos-1));
        console.log("New Node");
        console.log(val);
        if ( this._insertPos-2 > 0 ) {
            console.log("New Node Parent");
            var newNodeParent = this._arr[nodeParent(this._insertPos-1)];
            console.log(newNodeParent);
            // _attachNodes(this._insertPos-1, nodeParent(this._insertPos-1));
        }
        // compare and swim  if needed
        this.swimUp(this._insertPos-1);
    },
    _delLastLeaf: function delLastLeaf() {
        // delete Last Leaf
        // remove it
        // _delNodesRelation(this._arr.pop());
        //decerement the insert Position
        this._arr.pop();
        this._insertPos -= 1;
    },
    delMax: function delMin() {
        // Delete Maximum Node which is the Root Node
        if ( !this.isEmpty() ) {
            // delete the root Minimum Node
            // get last node which is the Max Node in Min Binary Heap at root - O(lgN)
            heapSwap(this._arr, 1, this._insertPos-1);
            // remove the last leaf - O(1)
            this._delLastLeaf();
            //rebalance the heap by sinking Down from root Index, 1. - O(lgN)
            this.sinkDown(1);
        }
    },
    seek: function seek (key) {
        // O(1)
        return (key<this._insertPos && key > 0)?this._arr[key]:undefined;
    },
    maxHeap: function minHeap() {
        // return maximum of maxHeap - O(1) which must be at Root Node
        return this.seek(1);
    },
    print: function print(log) {
        var list = [];
        this._arr.forEach(function loopArr(element, index, arr) {
            if ( index > 0 ) list.push(element);
        });
        log(list);
    },

    heapifyAll: function function_name() {
        // Recursively from bottom Node Tree to Root Node triangles heapify All
        for (var curPos = this._insertPos-1; curPos > 1;) {
            this.sinkDown(nodeParent(curPos));

            // efficient for comparison. only allow one of the children to compare
            // with parent node
            if ( nodeParent(curPos) === nodeParent(curPos-1) ) curPos -=2;
            else curPos--;
        }
    },
    // Heap Sort
    heapSort: function heapSort() {
        // In place unstable Sort
        // 1. swap last leaf and root node
        // 2. decrement last leaf pointer
        // 3. sink/sift down from root node
        // 4. repeat until heap size === 1

        // this is the current position of last leaf in array
        var
            limitCount = this._insertPos- 1,
            lastNode;

        // log("Starting heap sort");
        // log("limitCount starting at: "+limitCount);

        while ( limitCount > 1 ) {
            // log("limitCount is: "+ limitCount);
            // 1. swap last leaf and root node
            heapSwap(this._arr, 1, limitCount);

            // 2.
            // cut the last leaf relation from heap
            lastNode = this._arr[limitCount];

            // if ( lastNode.parent.leftChild === lastNode ) { lastNode.parent.leftChild = undefined; }
            // else if ( lastNode.parent.rightChild === lastNode ) { lastNode.parent.rightChild = undefined; }

            // log("last Node is: ");
            // log(lastNode);
            // log("lastNode.parent.leftChild " + (!!lastNode.parent.leftChild? lastNode.parent.leftChild.val: undefined));
            // log("lastNode.parent.rightChild " + (!!lastNode.parent.rightChild? lastNode.parent.rightChild.val: undefined));


            // log("before heap state ");
            // this.print(log);

            // 3. sink/sift down from root node
            //rebalance the heap by sinking Down from root Index, 1. - O(lgN)
            this.sinkDown(1, limitCount);

            // log("after heap state ");
            // this.print(log);

            // decrement last leaf pointer
            limitCount -= 1;
            // log("limitCount at: "+limitCount);
        }
    },
};

// for debugging and testing only
var log = console.log;

var dummy = function dummy() {
    // body...
    return;
};

console.log = (function (status) {
    if (status) return log;
    else return dummy;
})(false);

// var heap = Object.create(maxBinaryHeap);
// heap.init();
// heap.insert(100);
// heap.insert(-1000);
// heap.insert(-2000);
// heap.insert(20000);
// heap.insert(780);
// heap.insert(2340);
// // heap.print(log);
// console.assert(heap.maxHeap()==20000, "Should equal 20000");
// heap.print(log);
// log("------------------------");
// heap.delMax();
// console.assert(heap.maxHeap()==2340, "Should equal 2340");
// heap.print(log);
// heap.heapSort();
// heap.print(log);
// heap.insert(780);
// heap.print(log);
// heap.heapifyAll();
// heap.print(log);