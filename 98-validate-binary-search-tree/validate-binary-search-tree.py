# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # def validate(root, direction):
        #     val = root.val
        #     left = root.left
        #     right = root.right

        #     lrv = validate(left, direction) if left != None else (True, set())
        #     rtv = validate(right, direction) if right != None else (True, set())

        #     left_valid, left_l = lrv[0], lrv[1]
        #     right_valid, right_l = rtv[0], rtv[1]
            
        #     is_v = True if len(left_l) == 0 else val > max(left_l)
        #     is_v = True and is_v if len(right_l) == 0 else val < min(right_l) and is_v

        #     vtr = left_l + right_l + [val]
        #     print(val, left_valid, right_valid, left_l, right_l, vtr, is_v)

        #     if left_valid and right_valid:
        #         return (is_v, vtr)
        #     else:
        #         return (False, vtr)
        
        # valid, _ = validate(root, 'NA')
        # return valid

        def validate(node, low, high):
            if not node:
                return True
            
            if not low < node.val < high:
                return False

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        return validate(root, float('-inf'), float('inf'))
            
            
            




        