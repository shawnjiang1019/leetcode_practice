# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # get the height of the left tree
        # get the height of the right tree
        # check the height difference
        def getHeight(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            height = max(getHeight(root.left), getHeight(root.right)) + 1
            return height
        
        if not root:
            return True
        
        left_height = getHeight(root.left)
        right_height = getHeight(root.right)
        
        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)
        height_cond = abs(left_height - right_height) < 2
        return left_balanced and right_balanced and height_cond
        

        