from abc import ABC, abstractmethod
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class AbstractBinaryTree(ABC):
    # === Traversals ===
    @abstractmethod
    def inorderTraversal(self, root): pass

    @abstractmethod
    def preorderTraversal(self, root): pass

    @abstractmethod
    def postorderTraversal(self, root): pass

    @abstractmethod
    def levelOrderTraversal(self, root): pass

    @abstractmethod
    def zigzagLevelOrderTraversal(self, root): pass

    # === Binary Tree Construction and Modification ===
    @abstractmethod
    def insert(self, root, val): pass

    @abstractmethod
    def delete(self, root, val): pass

    # === Binary Tree Property Checks ===
    @abstractmethod
    def height(self, root): pass

    @abstractmethod
    def isBalanced(self, root): pass

    @abstractmethod
    def lowestCommonAncestorBT(self, root, p, q): pass

    @abstractmethod
    def countNodes(self, root): pass

    @abstractmethod
    def countLeaves(self, root): pass

    @abstractmethod
    def isSameTree(self, p, q): pass

    @abstractmethod
    def isSubtree(self, root, subRoot): pass

    # === Binary Search Trees ===
    @abstractmethod
    def insertIntoBST(self, root, val): pass

    @abstractmethod
    def deleteFromBST(self, root, key): pass

    @abstractmethod
    def searchBST(self, root, val): pass

    @abstractmethod
    def lowestCommonAncestorBST(self, root, p, q): pass

    # === Advanced Operations ===
    @abstractmethod
    def serialize(self, root): pass

    @abstractmethod
    def deserialize(self, data): pass

    @abstractmethod
    def invertTree(self, root): pass

    @abstractmethod
    def binaryTreePaths(self, root): pass

class BinaryTree(AbstractBinaryTree):
    # === Binary Tree Construction and Modification ===
    def insert(self, root, val):
        new_node = TreeNode(val)
        if not root:
            return new_node
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node.left:
                node.left = new_node
                return root
            queue.append(node.left)
            if not node.right:
                node.right = new_node
                return root
            queue.append(node.right)

    def delete(self, root, key):
        if not root:
            return None
        if not root.left and not root.right:
            return None if root.val == key else root

        key_node = None
        queue = deque([root])
        last_node = None
        while queue:
            last_node = queue.popleft()
            if last_node.val == key:
                key_node = last_node
            if last_node.left:
                queue.append(last_node.left)
            if last_node.right:
                queue.append(last_node.right)

        if key_node:
            key_node.val = last_node.val
            self._deleteDeepest(root, last_node)
        return root

    def _deleteDeepest(self, root, target):
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                if node.left == target:
                    node.left = None
                    return
                queue.append(node.left)
            if node.right:
                if node.right == target:
                    node.right = None
                    return
                queue.append(node.right)

    # === Traversals ===
    def inorderTraversal(self, root):
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    def preorderTraversal(self, root):
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []

    def postorderTraversal(self, root):
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []

    def levelOrderTraversal(self, root):
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

    def zigzagLevelOrderTraversal(self, root):
        if not root:
            return []
        
        queue = deque([root])
        res = []
        LTR = True

        while queue:
            level = deque()

            for i in range(len(queue)):
                node = queue.popleft()
                if LTR:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            res.append(list(level))
            LTR = not LTR
        
        return res

    # === Binary Tree Property Checks ===
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):
        def dfs(root):
            if not root:
                return [True, 0]
            
            L = dfs(root.left)
            R = dfs(root.right)

            b = L[0] and R[0] and (abs(L[1] - R[1]) <= 1)
            h = 1 + max(L[1], R[1])

            return [b, h]

        return dfs(root)[0]

    def lowestCommonAncestorBT(self, root, p, q):
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestorBT(root.left, p, q)
        right = self.lowestCommonAncestorBT(root.right, p, q)

        if left and right:
            return root
        
        return left or right

    def countNodes(self, root):
        if not root:
            return 0
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countLeaves(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return self.countLeaves(root.left) + self.countLeaves(root.right)

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root, subRoot):
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # === Binary Search Trees ===
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    def deleteFromBST(self, root, key):
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteFromBST(root.left, key)
        elif key > root.val:
            root.right = self.deleteFromBST(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            succ = root.right
            while succ.left:
                succ = succ.left
            root.val = succ.val
            root.right = self.deleteFromBST(root.right, succ.val)
        return root

    def searchBST(self, root, val):
        if not root or root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    def lowestCommonAncestorBST(self, root, p, q):
        if not root:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestorBST(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestorBST(root.right, p, q)
        return root

    # === Advanced Operations ===
    def serialize(self, root):
        if not root:
            return ""

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        return ', '.join(result)

    def deserialize(self, data):
        if not data:
            return None

        nodes = data.split(', ')
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1

        while queue:
            node = queue.popleft()

            # Left child
            if nodes[i] != "null":
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1

            # Right child
            if nodes[i] != "null":
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1

        return root

    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def binaryTreePaths(self, root):
        paths = []
        def dfs(node, path):
            if not node:
                return
            if not node.left and not node.right:
                paths.append(path + str(node.val))
            else:
                dfs(node.left, path + str(node.val) + "->")
                dfs(node.right, path + str(node.val) + "->")
        dfs(root, "")
        return paths
