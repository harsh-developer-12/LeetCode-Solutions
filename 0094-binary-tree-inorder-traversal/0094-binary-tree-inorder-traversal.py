# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode],Elements = None) -> List[int]:
        if Elements is None:
            Elements = []
        if root is None:
            return Elements
        
        self.inorderTraversal(root.left,Elements)
        Elements.append(root.val)
        self.inorderTraversal(root.right,Elements)
        return Elements