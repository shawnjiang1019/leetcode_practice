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
        def getHeight(root: Optional[TreeNode]) -> tuple:
            if not root:
                return (0, True)
            left_height, left_balanced = getHeight(root.left)
            right_height, right_balanced = getHeight(root.right)
            height = max(left_height, right_height) + 1
            if not left_balanced or not right_balanced:
                return (height, False)
            
            if abs(left_height - right_height) <= 1:
                return (height, True)
            return (height, False)
            
        return getHeight(root)[1]
        