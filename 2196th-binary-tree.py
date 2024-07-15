# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:
        children = set()
        nodes = {}
        
        for parent,child,left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            
            children.add(child)
        
        for i in descriptions:
            if i[0] not in children:
                return nodes[i[0]]   
        return None