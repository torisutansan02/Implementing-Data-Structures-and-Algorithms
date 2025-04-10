from tree import BinaryTree, TreeNode

def main():
    tree = BinaryTree()

    # === Binary Tree Sample ===
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Inorder:", tree.inorderTraversal(root))
    print("Preorder:", tree.preorderTraversal(root))
    print("Postorder:", tree.postorderTraversal(root))
    print("Level Order:", tree.levelOrderTraversal(root))
    print("Zigzag Level Order:", tree.zigzagLevelOrderTraversal(root))
    print("Height:", tree.height(root))
    print("Is Balanced:", tree.isBalanced(root))
    print("Count Nodes:", tree.countNodes(root))
    print("Count Leaves:", tree.countLeaves(root))
    print("Binary Tree Paths:", tree.binaryTreePaths(root))

    # === LCA (Binary Tree) ===
    node4 = root.left.left
    node5 = root.left.right
    lca_bt = tree.lowestCommonAncestorBT(root, node4, node5)
    print("LCA of 4 and 5 (BT):", lca_bt.val if lca_bt else None)

    # === Subtree & Same Tree ===
    subRoot = TreeNode(2)
    subRoot.left = TreeNode(4)
    subRoot.right = TreeNode(5)
    print("Is Subtree:", tree.isSubtree(root, subRoot))

    # === Invert and Serialize/Deserialize ===
    inverted = tree.invertTree(root)
    print("Inverted Level Order:", tree.levelOrderTraversal(inverted))
    serialized = tree.serialize(root)
    print("Serialized:", serialized)
    deserialized = tree.deserialize(serialized)
    print("Deserialized Inorder:", tree.inorderTraversal(deserialized))

    # === Binary Search Tree Sample ===
    bst = None
    for val in [5, 3, 6, 2, 4, 7]:
        bst = tree.insertIntoBST(bst, val)
    print("BST Inorder:", tree.inorderTraversal(bst))
    bst = tree.deleteFromBST(bst, 3)
    print("BST Inorder after deleting 3:", tree.inorderTraversal(bst))
    found = tree.searchBST(bst, 6)
    print("Search BST for 6:", found.val if found else None)
    lca_bst = tree.lowestCommonAncestorBST(bst, TreeNode(2), TreeNode(4))
    print("LCA of 2 and 4 (BST):", lca_bst.val if lca_bst else None)

if __name__ == "__main__":
    main()
