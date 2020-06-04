# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        x_info = []
        y_info = []
        depth = 0
        parent = None

        if root is None:
            return False

        self.dfs(root, x, y, depth, parent, x_info, y_info)

        if x_info[0][0] == y_info[0][0] and x_info[0][1] != y_info[0][1]:
            return True
        else:
            return False

    def dfs(self, root, x, y, depth, parent, x_info, y_info):
        if root is None:
            return False

        if root.val == x:
            x_info.append((depth, parent))

        if root.val == y:
            y_info.append((depth, parent))

        depth += 1
        self.dfs(root.left, x, y, depth, root, x_info, y_info)
        self.dfs(root.right, x, y, depth, root, x_info, y_info)