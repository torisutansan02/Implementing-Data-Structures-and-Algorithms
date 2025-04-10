from abc import ABC, abstractmethod
from collections import deque

# Abstract Binary Tree Interface
class AbstractBinaryTree(ABC):
    @abstractmethod
    def insert(self, val): pass

    @abstractmethod
    def delete(self, val): pass

    @abstractmethod
    def search(self, val): pass

    @abstractmethod
    def inorder(self, root): pass

    @abstractmethod
    def preorder(self, root): pass

    @abstractmethod
    def postorder(self, root): pass

    @abstractmethod
    def levelOrder(self, root): pass

    @abstractmethod
    def __str__(self): pass

# Node class (TreeNode for LeetCode compatibility)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# BinaryTree with LeetCode-style methods
class BinaryTree(AbstractBinaryTree):
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(node, val):
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, val)

    def delete(self, val):
        def _delete(node, val):
            if not node:
                return None
            if val < node.val:
                node.left = _delete(node.left, val)
            elif val > node.val:
                node.right = _delete(node.right, val)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                # Find inorder successor
                succ = node.right
                while succ.left:
                    succ = succ.left
                node.val = succ.val
                node.right = _delete(node.right, succ.val)
            return node

        self.root = _delete(self.root, val)

    def search(self, val):
        def _search(node, val):
            if not node:
                return False
            if node.val == val:
                return True
            return _search(node.left, val) or _search(node.right, val)

        return _search(self.root, val)

    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

    def preorder(self, root):
        return [root.val] + self.preorder(root.left) + self.preorder(root.right) if root else []

    def postorder(self, root):
        return self.postorder(root.left) + self.postorder(root.right) + [root.val] if root else []

    def levelOrder(self, root):
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def __str__(self):
        return str(self.levelOrder(self.root))
