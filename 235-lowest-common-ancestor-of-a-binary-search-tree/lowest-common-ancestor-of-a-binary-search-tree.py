# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def get_lca(node, p_val, q_val):
            if node is None:
                return node
            
            node_val = node.val

            if p_val <= node_val and q_val >= node_val:
                return node
            
            if p_val >= node_val and q_val <= node_val:
                return node
            
            if p_val < node_val and q_val < node_val:
                return get_lca(node.left, p_val, q_val)
            
            if p_val > node_val and q_val > node_val:
                return get_lca(node.right, p_val, q_val)
        
        return get_lca(root, p.val, q.val)