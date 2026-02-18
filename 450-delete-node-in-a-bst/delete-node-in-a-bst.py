# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # find the leftmost node in the right subtree
        cur = root
        parent = None
        while cur and cur.val != key:
            parent = cur
            if cur.val < key:
                cur = cur.right
            else:
                cur = cur.left
        
        if not cur:
            return root
        
        if not parent:
            if not cur.left and not cur.right:
                return None
            if cur.left and not cur.right:
                return cur.left
            if not cur.left and cur.right:
                return cur.right
            else:
                p = cur.right
                succ_p = cur
                while p.left:
                    succ_p = p
                    p = p.left
                cur.val = p.val
                if succ_p == cur:
                    succ_p.right = p.right
                else:
                    succ_p.left = p.right
                return root

        if not cur.left and not cur.right:
            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None
        elif cur.left and cur.right:
            # find leftmost in the right subtree
            p = cur.right
            succ_p = cur
            while p.left:
                succ_p = p
                p = p.left
            cur.val = p.val
            if succ_p == cur:
                succ_p.right = p.right
            else:
                succ_p.left = p.right

        else:
            if cur.left and not cur.right:
                if cur.val < parent.val:
                    parent.left = cur.left
                else:
                    parent.right = cur.left
            else:
                if cur.val < parent.val:
                    parent.left = cur.right
                else:
                    parent.right = cur.right

        return root