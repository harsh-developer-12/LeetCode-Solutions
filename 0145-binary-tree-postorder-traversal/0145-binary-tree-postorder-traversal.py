# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode],Elements=None) -> List[int]:
        if Elements is None:
            Elements = []
        if root is None:
            return Elements
        
        self.postorderTraversal(root.left,Elements)
        self.postorderTraversal(root.right,Elements)
        Elements.append(root.val)
        return Elements