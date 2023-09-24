# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        def traverse(root):
            left = root.left
            right = root.right

            if left == None and right == None:
                return
            elif  left == None:
                l.append(right.val)
                traverse(right)
            elif right == None:
                l.append(left.val)
                traverse(left)
            else:
                traverse(left)
                traverse(right)
        traverse(root)
        return l
            

        