const { Stack, Queue, LinkedList, BinarySearchTree } = require('./index');

// --- Stack Example: Reverse a string ---
function reverseString(str) {
  const stack = new Stack();
  for (const char of str) {
    stack.push(char);
  }

  let reversedStr = '';
  while (stack.peek() !== undefined) {
    reversedStr += stack.pop();
  }

  return reversedStr;
}

console.log('--- Stack Example: Reverse a string ---');
const originalString = 'hello';
const reversed = reverseString(originalString);
console.log(`Original: ${originalString}`);
console.log(`Reversed: ${reversed}`); // olleh
console.log('\\n');

// --- Queue Example: Implement a simple "printer queue" ---
class PrinterQueue {
    constructor() {
      this.queue = new Queue();
    }
  
    addJob(job) {
      console.log(`Adding job to queue: ${job}`);
      this.queue.enqueue(job);
    }
  
    processJobs() {
      console.log('Processing all jobs in the queue:');
      while (this.queue.data.length > 0) {
        const job = this.queue.dequeue();
        console.log(`Printing: ${job}`);
      }
      console.log('All jobs processed.');
    }
  }

console.log('--- Queue Example: Printer Queue ---');
const printer = new PrinterQueue();
printer.addJob('Document1.pdf');
printer.addJob('Image.png');
printer.addJob('Spreadsheet.xlsx');
printer.processJobs();
console.log('\\n');


// --- LinkedList Example: Find the middle node ---
function findMidpoint(list) {
    let slow = list.getFirst();
    let fast = list.getFirst();
  
    while (fast.next && fast.next.next) {
      slow = slow.next;
      fast = fast.next.next;
    }
  
    return slow;
  }

console.log('--- LinkedList Example: Find Midpoint ---');
const list = new LinkedList();
list.insertLast('a');
list.insertLast('b');
list.insertLast('c');
list.insertLast('d');
list.insertLast('e');
const midpoint = findMidpoint(list);
console.log(`Midpoint of the list is: ${midpoint.data}`); // c
console.log('\\n');

// --- BinarySearchTree Example: Validate a BST ---
function validate(node, min = null, max = null) {
    if (max !== null && node.data > max) {
      return false;
    }
  
    if (min !== null && node.data < min) {
      return false;
    }
  
    if (node.left && !validate(node.left, min, node.data)) {
      return false;
    }
  
    if (node.right && !validate(node.right, node.data, max)) {
      return false;
    }
  
    return true;
  }

console.log('--- BinarySearchTree Example: Validate BST ---');
const bst = new BinarySearchTree();
bst.insert(10);
bst.insert(5);
bst.insert(15);
bst.insert(0);
bst.insert(7);
bst.insert(12);
bst.insert(20);

console.log('Is the tree a valid BST?', validate(bst.root)); // true

// Create an invalid BST
const invalidBst = new BinarySearchTree();
invalidBst.root = new Node(10);
invalidBst.root.left = new Node(5);
invalidBst.root.right = new Node(15);
invalidBst.root.left.right = new Node(20); // Invalid node

console.log('Is the second tree a valid BST?', validate(invalidBst.root)); // false
