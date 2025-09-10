# Data Structures Master Lesson… EDIP 90-Minute Plan

**Lesson Contents**

| Topic | Code | Tests | Lesson Notes |
|---|---|---|---|
| Linked List, Stack, Queue | [`index.js`](./index.js), [`data_structures.py`](./data_structures.py) | [`test.js`](./test.js), [`test_data_structures.py`](./test_data_structures.py) | [See Part A](#part-a-explain) |
| Binary Search Trees | [`index.js`](./index.js), [`data_structures.py`](./data_structures.py) | [`test.js`](./test.js), [`test_data_structures.py`](./test_data_structures.py) | [See Part B](#part-b-binary-search-trees-deep-dive) |
| Demos & Algorithms | [`examples.js`](./examples.js) | - | [See Part C](#part-c-demonstrate) |
| AVL Tree Lab | *Student Task* | *Student Task* | [Lesson](./trees-labs/balancing-a-binary-tree/README.md) \| [Solution](./trees-labs/solution/avl-tree.md) |

> Fork and clone this repo. You will **not** write code live. You will read, run, trace, and extend what is already here. The lab focuses on **AVL self-balancing**.

---

## Prereqs and Setup

**You need:** Node 18+, npm, and a terminal.

**Install and run:**

```bash
# from your fork
npm i 

# run the examples
node examples.js

# run tests
npm run test
python3 -m unittest test_data_structures.py
python -m unittest test_data_structures.py 
```

---

## Learning Objectives

By the end of this session you will be able to:
* Explain core structures: Linked List, Stack, Queue, Binary Search Tree.
* Run and trace BFS and DFS on a BST and predict visit order.
* Describe insert, find, delete in a BST including edge cases.
* Explain why balancing matters and how AVL rotations fix skew.
* Map real problems to the right structure and traversal.
* Name key Gang of Four patterns and when to apply them.

---

## 90-Minute EDIP Timeline

**0 to 10** Explain… Why data structures matter. Big O at a glance.  
**10 to 25** Explain… Linked List, Stack, Queue in context. Quick demos.  
**25 to 35** Demonstrate… Build intuition for BST invariants and shape.  
**35 to 55** Imitate… Students trace BFS and DFS variants on real code.  
**55 to 70** Explain then Demonstrate… BST delete and validation pitfalls.  
**70 to 85** Practice… AVL Lab. Implement rotations and verify balance.  
**85 to 90** Explain… Gang of Four patterns. Connect DS to design choices.

Time boxes are strict. Keep the energy high. Use the provided prompts.

---

## Part A… Explain

### What is a Data Structure
A structure organizes data so operations are efficient. Choose a structure to win constant factors and asymptotics. Pick the tool that matches access patterns.

### Quick Review… Linked List, Stack, Queue
**Linked List**
* Node holds `data` and `next`. Simple insert at head is O(1).
* Random access is O(n). Traversal is linear.
* See `LinkedList` API for insertFirst, getLast, insertAt, removeAt.

**Stack**
* LIFO. Push and pop from one end.
* Call stacks. Undo stacks. Expression evaluation.

**Queue**
* FIFO. Enqueue to back. Dequeue from front.
* Schedulers and breadth-first traversals.

**Complexities**
| Structure | Access | Search | Insert | Delete |
|---|---|---|---|---|
| Linked List | O(n) | O(n) | O(1) at head | O(1) at head |
| Stack | O(n) casual access… O(1) peek | O(n) | O(1) | O(1) |
| Queue | O(n) casual access… O(1) head | O(n) | O(1) | O(1) |

Why these matter… If you need order of arrival use a queue. If you need last change first use a stack. If you mutate many middle elements an array may be better than a singly linked list. If you need sorted retrieval and fast search move to trees.

---

## Part B… Binary Search Trees Deep Dive

### BST Invariant
For any node with value `x`… all values in the left subtree are less than `x`. All values in the right subtree are greater than `x`. This invariant enables binary search on structure… not on arrays.

### Core Operations

**Insert**
Walk from root. Compare. Go left if less. Go right if greater. Stop at null and attach.
* Average time O(log n) if height is logarithmic.
* Worst time O(n) if the tree degenerates into a line.

**Find or Contains**
Same walk. Stop when match or when you fall off the tree.

**Delete**
Three cases.  
1. Leaf… remove directly.  
2. One child… splice child into the deleted spot.  
3. Two children… replace value with inorder successor then delete successor from right subtree.

**Validate BST**
Use min or max guard while descending. When you go left update `max`. When you go right update `min`. A simple local check on parent and child is not enough.

### Traversals at a Glance

**Breadth First Search**
Use a queue. Visit nodes level by level. Great when the target is near the root or when you need shortest paths by edge count.

**Depth First Search**
Use recursion or an explicit stack.
* **Preorder** root then left then right. Prebuild tasks or serialize structure.
* **Inorder** left then root then right. Sorted order for BSTs. This is how you stream sorted data.
* **Postorder** left then right then root. Useful for deletes and frees.

**Orders by example** for the tree with root 10 and children 5 and 15 then 3 and 7 then 12 and 18.
* BFS… 10 5 15 3 7 12 18
* Preorder… 10 5 3 7 15 12 18
* Inorder… 3 5 7 10 12 15 18
* Postorder… 3 7 5 12 18 15 10

### Choosing BFS or DFS
Pick BFS if a shallow answer exists or you need level order. Pick DFS when memory is tight on wide trees or when you need dependency style evaluation. Both are O(n) visits. Different space costs and visit orders.

---

## Part C… Demonstrate

Run the demo script.

```bash
node examples.js
```

Observe:
* Stack reverses a string by pushing characters then popping.
* Queue simulates a printer by enqueuing jobs then dequeuing.
* Linked List midpoint uses the classic tortoise and hare.
* BST validation uses a min… max gate to ensure ordering.

Now instrument one traversal. Add `console.log` in a DFS and watch the order. Remove the logs after.

---

## Part D… Imitate

Students trace traversals by hand. Then confirm with code.

1. Build this tree by calling `insert`: 10 5 15 3 7 12 18.  
2. Predict BFS and each DFS order on paper.  
3. Run the matching methods and compare.  
4. Delete 5. Predict the shape. Confirm with `dfsInOrder` sorted output.  
5. Validate the tree. Explain why validation passes or fails after edits.

Shell hints…

```js
const { BinarySearchTree } = require('./index');
const tree = new BinarySearchTree();
[10,5,15,3,7,12,18].forEach(v => tree.insert(v));
console.log('BFS', tree.bfs());
console.log('Pre', tree.dfsPreOrder());
console.log('In ', tree.dfsInOrder());
console.log('Post', tree.dfsPostOrder());
tree.delete(5);
console.log('After delete inorder', tree.dfsInOrder());
```

---

## Part E… Practice Lab… AVL Balancing

**Goal** keep height near log n for steady O(log n) operations. A skewed BST behaves like a list.

**Steps**
1. Read `avl-tree.md` for height, balance factor, and rotation visuals.  
2. Open the provided `AVLTree` skeleton. Implement `rotateLeft`, `rotateRight`, height maintenance, and rebalancing checks while unwinding from an insert.  
3. Insert an increasing sequence for example 1..9 and confirm rotations occur.  
4. Verify inorder traversal still returns sorted values.  
5. Add tests that prove balance factor bound of absolute value less or equal to 1 at every node.

**Checks**
* Left Left imbalance… single right rotation.
* Right Right imbalance… single left rotation.
* Left Right imbalance… left rotation on child then right rotation.
* Right Left imbalance… right rotation on child then left rotation.

**Stretch**
Compare performance by timing unbalanced insert then balanced insert across 10k random integers. Observe height and operation count.

---

## How we solve problems with these structures

Patterns to choose:
* Many appends with occasional traversal… Linked List at head is simple.
* Last change wins behavior… Stack.
* Producer consumer pipelines… Queue.
* Sorted reads and fast search… BST or a balanced variant. Use inorder to stream sorted data.
* When worst case matters… pick a self balancing tree like AVL or Red Black.

Checklist:
* What operations dominate count.  
* Do you need order kept or only membership.  
* What are worst case constraints.  
* What memory headroom do you have.  
* How predictable is input order. If nearly sorted then always balance.

---

## Gang of Four Patterns… micro map to this lesson

**Iterator** traverse collections uniformly. Your DFS and BFS are iterators in spirit.  
**Composite** treat trees of nodes as a single whole. A BST is a natural composite.  
**Strategy** swap traversal strategy BFS vs DFS without changing the tree.  
**Factory Method** centralize Node creation when variants appear height tracked nodes vs plain.  
**Visitor** separate operations from structure. Example a HeightVisitor or ValidateVisitor that walks a tree.  
**Observer** optional… emit events on insert or delete so views can update.  
**Adapter** wrap array or list as a queue or stack when a consumer expects that interface.  
**Template Method** define the high level delete algorithm and let subclasses provide rotation details for AVL vs Red Black.

Takeaway… data structures shape data. Patterns shape the code that uses the data. Together they make systems fast and clean.

---

## Instructor Prompts and Cold Calls

* Why does inorder traversal return sorted values on a BST.  
* Show a case where DFS uses less memory than BFS.  
* Walk the three delete cases and name the first broken invariant if you forget the successor step.  
* Why is min… max validation safer than only checking parent and child.  
* Which rotation fixes a Right Left imbalance. Explain the two step reasoning.

---

## Exit Ticket

* In one sentence… when do you choose BFS over DFS.  
* What is the role of inorder successor in delete.  
* Name one GoF pattern and how you would map it to trees.

---

## References in this repo

* `index.js` Linked List, Stack, Queue, BST implementation used in class.  
* `examples.js` runnable mini demos.  
* `test.js` Jest specs.  
* `binary-tree.md` reference explainer.  
* `avl-tree.md` balancing lab with rotation visuals.

---

## Appendix… Minimal Pseudocode

**BFS**

```
queue = [root]
while queue not empty:
  node = queue.pop_front()
  visit(node)
  if node.left: queue.push_back(node.left)
  if node.right: queue.push_back(node.right)
```

**Inorder DFS**

```
def inorder(node):
  if node is null: return
  inorder(node.left)
  visit(node)
  inorder(node.right)
```

**Validate BST with min… max**

```
def valid(node, min = -inf, max = +inf):
  if node is null: return true
  if node.value <= min or node.value >= max: return false
  return valid(node.left, min, node.value) and valid(node.right, node.value, max)
```

Be precise. Think in invariants. Trace slowly. Then run fast.
