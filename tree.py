from linked_list import LinkedList

class TreeNode:
    """Node for a rooted tree, with a linked list of children."""
    def __init__(self, data):
        self.data = data
        self.children = LinkedList()

    def add_child(self, node):
        """Add a TreeNode as a child."""
        self.children.insert_at_tail(node)

    def __str__(self):
        return str(self.data)

class Tree:
    """Rooted tree with preorder traversal and find operation."""
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def _traverse_preorder(self, node, visit):
        if node:
            visit(node)
            for child in node.children.traverse():
                self._traverse_preorder(child, visit)

    def traverse_preorder(self, visit):
        """Perform a preorder traversal, calling visit on each node."""
        self._traverse_preorder(self.root, visit)

    def find(self, data):
        """Find first node with matching data."""
        result = None
        def check(node):
            nonlocal result
            if node.data == data:
                result = node
        self.traverse_preorder(check)
        return result
