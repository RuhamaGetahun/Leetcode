# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if node is None:
                return False 
            
            if not node.right and not node.left:
                return currSum + node.val == targetSum

            left= dfs(node.left, currSum + node.val)
            right = dfs(node.right, currSum + node.val)
            return left or right 

        return dfs(root, 0)