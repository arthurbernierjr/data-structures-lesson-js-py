const { BinarySearchTree, Node, LinkedList, Stack, Queue } = require('./index');

describe('LinkedList', () => {
  test('insertFirst', () => {
    const list = new LinkedList();
    list.insertFirst(1);
    expect(list.head.data).toBe(1);
    list.insertFirst(2);
    expect(list.head.data).toBe(2);
  });

  test('size', () => {
    const list = new LinkedList();
    list.insertFirst(1);
    list.insertFirst(1);
    expect(list.size()).toBe(2);
  });

  test('getFirst', () => {
    const list = new LinkedList();
    list.insertFirst(1);
    list.insertFirst(2);
    expect(list.getFirst().data).toBe(2);
  });

  test('getLast', () => {
    const list = new LinkedList();
    list.insertFirst(1);
    list.insertFirst(2);
    expect(list.getLast().data).toBe(1);
  });

  test('clear', () => {
    const list = new LinkedList();
    list.insertFirst(1);
    list.insertFirst(1);
    list.clear();
    expect(list.size()).toBe(0);
  });

  test('removeFirst', () => {
    const list = new LinkedList();
    list.insertFirst(1);
    list.insertFirst(2);
    list.removeFirst();
    expect(list.size()).toBe(1);
    expect(list.getFirst().data).toBe(1);
  });

  test('removeLast', () => {
    const list = new LinkedList();
    list.insertFirst('a');
    list.insertFirst('b');
    list.removeLast();
    expect(list.size()).toBe(1);
    expect(list.getLast().data).toBe('b');
  });

  test('insertLast', () => {
    const list = new LinkedList();
    list.insertFirst('a');
    list.insertLast('b');
    expect(list.getLast().data).toBe('b');
  });

  test('getAt', () => {
    const list = new LinkedList();
    list.insertLast(1);
    list.insertLast(2);
    expect(list.getAt(0).data).toBe(1);
    expect(list.getAt(1).data).toBe(2);
  });

  test('removeAt', () => {
    const list = new LinkedList();
    list.insertLast(1);
    list.insertLast(2);
    list.insertLast(3);
    list.removeAt(1);
    expect(list.getAt(1).data).toBe(3);
  });

  test('insertAt', () => {
    const list = new LinkedList();
    list.insertLast(1);
    list.insertLast(2);
    list.insertLast(3);
    list.insertAt(4, 1);
    expect(list.getAt(1).data).toBe(4);
  });
});

describe('Stack', () => {
    test('push, pop, and peek', () => {
      const s = new Stack();
      s.push(1);
      expect(s.peek()).toBe(1);
      s.push(2);
      expect(s.peek()).toBe(2);
      expect(s.pop()).toBe(2);
      expect(s.peek()).toBe(1);
      expect(s.pop()).toBe(1);
    });
  });
  
  describe('Queue', () => {
    test('enqueue and dequeue', () => {
      const q = new Queue();
      q.enqueue(1);
      q.enqueue(2);
      expect(q.dequeue()).toBe(1);
      expect(q.dequeue()).toBe(2);
    });
  });

describe('BinarySearchTree', () => {
  let tree;

  beforeEach(() => {
    tree = new BinarySearchTree();
  });

  describe('insert', () => {
    test('should insert a node in an empty tree', () => {
      tree.insert(10);
      expect(tree.root.value).toBe(10);
    });

    test('should insert smaller values to the left', () => {
      tree.insert(10);
      tree.insert(5);
      expect(tree.root.left.value).toBe(5);
    });

    test('should insert larger values to the right', () => {
      tree.insert(10);
      tree.insert(15);
      expect(tree.root.right.value).toBe(15);
    });

    test('should not insert duplicate values', () => {
      tree.insert(10);
      const result = tree.insert(10);
      expect(tree.root.left).toBeNull();
      expect(tree.root.right).toBeNull();
      expect(result).toBeUndefined();
    });

    test('should build a complex tree correctly', () => {
      tree.insert(10);
      tree.insert(5);
      tree.insert(15);
      tree.insert(3);
      tree.insert(7);
      tree.insert(12);
      tree.insert(18);
      
      expect(tree.root.value).toBe(10);
      expect(tree.root.left.value).toBe(5);
      expect(tree.root.right.value).toBe(15);
      expect(tree.root.left.left.value).toBe(3);
      expect(tree.root.left.right.value).toBe(7);
      expect(tree.root.right.left.value).toBe(12);
      expect(tree.root.right.right.value).toBe(18);
    });
  });

  describe('find', () => {
    beforeEach(() => {
      tree.insert(10);
      tree.insert(5);
      tree.insert(15);
    });

    test('should return the node if found', () => {
      const foundNode = tree.find(5);
      expect(foundNode.value).toBe(5);
    });

    test('should return undefined if the node is not found', () => {
      const result = tree.find(100);
      expect(result).toBeUndefined();
    });

    test('should handle searching in an empty tree', () => {
      const emptyTree = new BinarySearchTree();
      const result = emptyTree.find(1);
      expect(result).toBeUndefined();
    });
  });

  describe('delete', () => {
    beforeEach(() => {
      tree.insert(10);
      tree.insert(5);
      tree.insert(15);
      tree.insert(3);
      tree.insert(7);
      tree.insert(12);
      tree.insert(18);
    });

    test('should not change the tree if the node to be deleted is not found', () => {
      const initialOrder = tree.dfsInOrder();
      tree.delete(100);
      expect(tree.dfsInOrder()).toEqual(initialOrder);
    });

    test('should delete a leaf node', () => {
      tree.delete(3);
      expect(tree.find(3)).toBeUndefined();
    });

    test('should delete a node with one right child', () => {
      tree.insert(4);
      tree.delete(3);
      expect(tree.find(3)).toBeUndefined();
      expect(tree.root.left.left.value).toBe(4);
    });

    test('should delete a node with one left child', () => {
      tree.insert(2);
      tree.delete(3);
      expect(tree.find(3)).toBeUndefined();
      expect(tree.root.left.left.value).toBe(2);
    });

    test('should delete a node with two children', () => {
      tree.delete(5);
      expect(tree.find(5)).toBeUndefined();
      expect(tree.root.left.value).toBe(7);
      expect(tree.root.left.left.value).toBe(3);
    });

    test('should delete the root node', () => {
      tree.delete(10);
      expect(tree.find(10)).toBeUndefined();
      expect(tree.root.value).toBe(12);
    });

    test('should handle deleting from an empty tree', () => {
        const emptyTree = new BinarySearchTree();
        emptyTree.delete(1);
        expect(emptyTree.root).toBeNull();
    });
  });

  describe('Traversals', () => {
    beforeEach(() => {
      tree.insert(10);
      tree.insert(5);
      tree.insert(15);
      tree.insert(3);
      tree.insert(7);
      tree.insert(12);
      tree.insert(18);
    });
  
    test('dfsPreOrder', () => {
      const expectedOrder = [10, 5, 3, 7, 15, 12, 18];
      expect(tree.dfsPreOrder()).toEqual(expectedOrder);
    });

    test('dfsInOrder', () => {
      const expectedOrder = [3, 5, 7, 10, 12, 15, 18];
      expect(tree.dfsInOrder()).toEqual(expectedOrder);
    });

    test('dfsPostOrder', () => {
      const expectedOrder = [3, 7, 5, 12, 18, 15, 10];
      expect(tree.dfsPostOrder()).toEqual(expectedOrder);
    });

    test('bfs', () => {
      const expectedOrder = [10, 5, 15, 3, 7, 12, 18];
      expect(tree.bfs()).toEqual(expectedOrder);
    });
  });
});
