import logging
import sys

from array import Array
from matrix import Matrix
from stack import Stack
from queue import Queue
from linked_list import LinkedList
from tree import Tree, TreeNode

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Counters
total_tests = 0
passed_tests = 0
failed_tests = 0


def record_result(name, passed, message=None):
    global total_tests, passed_tests, failed_tests
    total_tests += 1
    if passed:
        passed_tests += 1
        logging.info("[PASS] %s", name)
    else:
        failed_tests += 1
        logging.error("[FAIL] %s - %s", name, message)


def test_array():
    name = 'Array basic operations'
    try:
        arr = Array()
        arr.insert(0, 'x')
        assert arr.access(0) == 'x'
        arr.insert(1, 'y')
        assert arr.size() == 2
        removed = arr.delete(0)
        assert removed == 'x'
        assert arr.access(0) == 'y'
        record_result(name, True)
    except Exception as e:
        record_result(name, False, str(e))


def test_matrix():
    name = 'Matrix row and element operations'
    try:
        m = Matrix(2, 3, 0)
        m.set(1, 2, 5)
        assert m.get(1, 2) == 5
        orig_rows, orig_cols = m.size()
        m.insert_row(1, [1, 1, 1])
        assert m.size()[0] == orig_rows + 1
        deleted = m.delete_row(1)
        assert deleted == [1, 1, 1]
        record_result(name, True)
    except Exception as e:
        record_result(name, False, str(e))


def test_stack():
    name = 'Stack push/pop/peek'
    try:
        s = Stack()
        s.push(10)
        s.push(20)
        assert s.peek() == 20
        val = s.pop()
        assert val == 20
        assert not s.is_empty() and s.size() == 1
        record_result(name, True)
    except Exception as e:
        record_result(name, False, str(e))


def test_queue():
    name = 'Queue enqueue/dequeue/front'
    try:
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')
        assert q.front() == 'a'
        val = q.dequeue()
        assert val == 'a'
        assert q.size() == 1
        record_result(name, True)
    except Exception as e:
        record_result(name, False, str(e))


def test_linked_list():
    name = 'LinkedList insert/delete/traverse'
    try:
        ll = LinkedList()
        ll.insert_at_head(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        vals = list(ll.traverse())
        assert vals == [1, 2, 3]
        assert ll.delete(2) is True
        assert list(ll.traverse()) == [1, 3]
        deleted_value = ll.delete_at_index(1)
        assert deleted_value == 3
        record_result(name, True)
    except Exception as e:
        record_result(name, False, str(e))


def test_tree():
    name = 'Tree add_child/find/traverse'
    try:
        tree = Tree('root')
        child1 = TreeNode('c1')
        child2 = TreeNode('c2')
        tree.root.add_child(child1)
        tree.root.add_child(child2)
        found = tree.find('c2')
        assert found is child2
        visited = []
        tree.traverse_preorder(lambda node: visited.append(node.data))
        assert visited == ['root', 'c1', 'c2']
        record_result(name, True)
    except Exception as e:
        record_result(name, False, str(e))


def main():
    logging.info("Starting data structure tests...")
    test_array()
    test_matrix()
    test_stack()
    test_queue()
    test_linked_list()
    test_tree()
    logging.info("Tests completed: %d/%d passed, %d failed.", passed_tests, total_tests, failed_tests)
    if failed_tests > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
