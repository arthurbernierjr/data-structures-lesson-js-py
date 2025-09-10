import unittest
from data_structures import (
    BinarySearchTree,
    BSTNode,
    LinkedList,
    Node,
    Stack,
    Queue,
)

class TestLinkedList(unittest.TestCase):
    def test_insert_first(self):
        ll = LinkedList()
        ll.insert_first(1)
        self.assertEqual(ll.head.data, 1)
        ll.insert_first(2)
        self.assertEqual(ll.head.data, 2)

    def test_size(self):
        ll = LinkedList()
        ll.insert_first(1)
        ll.insert_first(1)
        self.assertEqual(ll.size(), 2)

    def test_get_first(self):
        ll = LinkedList()
        ll.insert_first(1)
        ll.insert_first(2)
        self.assertEqual(ll.get_first().data, 2)

    def test_get_last(self):
        ll = LinkedList()
        ll.insert_first(1)
        ll.insert_first(2)
        self.assertEqual(ll.get_last().data, 1)

    def test_clear(self):
        ll = LinkedList()
        ll.insert_first(1)
        ll.insert_first(1)
        ll.clear()
        self.assertEqual(ll.size(), 0)

    def test_remove_first(self):
        ll = LinkedList()
        ll.insert_first(1)
        ll.insert_first(2)
        ll.remove_first()
        self.assertEqual(ll.size(), 1)
        self.assertEqual(ll.get_first().data, 1)

    def test_remove_last(self):
        ll = LinkedList()
        ll.insert_first("a")
        ll.insert_first("b")
        ll.remove_last()
        self.assertEqual(ll.size(), 1)
        self.assertEqual(ll.get_last().data, "b")

    def test_insert_last(self):
        ll = LinkedList()
        ll.insert_first("a")
        ll.insert_last("b")
        self.assertEqual(ll.get_last().data, "b")

    def test_get_at(self):
        ll = LinkedList()
        ll.insert_last(1)
        ll.insert_last(2)
        self.assertEqual(ll.get_at(0).data, 1)
        self.assertEqual(ll.get_at(1).data, 2)

    def test_remove_at(self):
        ll = LinkedList()
        ll.insert_last(1)
        ll.insert_last(2)
        ll.insert_last(3)
        ll.remove_at(1)
        self.assertEqual(ll.get_at(1).data, 3)

    def test_insert_at(self):
        ll = LinkedList()
        ll.insert_last(1)
        ll.insert_last(2)
        ll.insert_last(3)
        ll.insert_at(4, 1)
        self.assertEqual(ll.get_at(1).data, 4)

class TestStack(unittest.TestCase):
    def test_push_pop_peek(self):
        s = Stack()
        s.push(1)
        self.assertEqual(s.peek(), 1)
        s.push(2)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.pop(), 1)
        self.assertIsNone(s.peek())

class TestQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(70)
        self.bst.insert(60)
        self.bst.insert(80)

    def test_insert(self):
        self.assertEqual(self.bst.root.value, 50)
        self.assertEqual(self.bst.root.left.value, 30)
        self.assertEqual(self.bst.root.left.left.value, 20)
        self.assertEqual(self.bst.root.left.right.value, 40)
        self.assertEqual(self.bst.root.right.value, 70)
        self.assertEqual(self.bst.root.right.left.value, 60)
        self.assertEqual(self.bst.root.right.right.value, 80)
        # Test inserting duplicate
        self.assertIsNone(self.bst.insert(50))

    def test_find(self):
        self.assertIsNotNone(self.bst.find(40))
        self.assertEqual(self.bst.find(40).value, 40)
        self.assertIsNone(self.bst.find(100))
        
        empty_tree = BinarySearchTree()
        self.assertIsNone(empty_tree.find(1))

    def test_contains(self):
        self.assertTrue(self.bst.contains(40))
        self.assertFalse(self.bst.contains(100))
        
        empty_tree = BinarySearchTree()
        self.assertFalse(empty_tree.contains(1))

    def test_delete(self):
        # Delete leaf node
        self.bst.delete(20)
        self.assertEqual(self.bst.dfs_in_order(), [30, 40, 50, 60, 70, 80])
        
        # Delete node with one child
        self.bst.insert(25)
        self.bst.delete(30)
        self.assertEqual(self.bst.dfs_in_order(), [25, 40, 50, 60, 70, 80])

        # Delete node with two children
        self.bst.delete(50)
        self.assertEqual(self.bst.dfs_in_order(), [25, 40, 60, 70, 80])
        self.assertEqual(self.bst.root.value, 60)

        # Delete root node again
        self.bst.delete(60)
        self.assertEqual(self.bst.dfs_in_order(), [25, 40, 70, 80])
        self.assertEqual(self.bst.root.value, 70)
        
        # Delete non-existent node
        initial_order = self.bst.dfs_in_order()
        self.bst.delete(100)
        self.assertEqual(self.bst.dfs_in_order(), initial_order)

        # Empty the tree
        self.bst.delete(70)
        self.bst.delete(80)
        self.bst.delete(25)
        self.bst.delete(40)
        self.assertIsNone(self.bst.root)

    def test_traversals(self):
        self.assertEqual(self.bst.dfs_in_order(), [20, 30, 40, 50, 60, 70, 80])
        self.assertEqual(self.bst.dfs_pre_order(), [50, 30, 20, 40, 70, 60, 80])
        self.assertEqual(self.bst.dfs_post_order(), [20, 40, 30, 60, 80, 70, 50])

    def test_bfs(self):
        self.assertEqual(self.bst.bfs(), [50, 30, 70, 20, 40, 60, 80])
        empty_tree = BinarySearchTree()
        self.assertEqual(empty_tree.bfs(), [])

if __name__ == '__main__':
    unittest.main()
