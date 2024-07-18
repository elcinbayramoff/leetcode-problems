Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
    

        
        to_delete_set = set(to_delete)
        remaining_trees = []

        def helper(node, is_root):
            if not node:
                return None
            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                remaining_trees.append(node)
            node.left = helper(node.left, root_deleted)
            node.right = helper(node.right, root_deleted)
            return None if root_deleted else node

        helper(root, True)
        return remaining_trees