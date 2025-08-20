# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        # In- orde == ordered 
        # pre-order == before 
        # post-order == left and right and then node 
        def dfs(node):
            nonlocal res
            if node is None:
                return 
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res[k -1]

            
        



        