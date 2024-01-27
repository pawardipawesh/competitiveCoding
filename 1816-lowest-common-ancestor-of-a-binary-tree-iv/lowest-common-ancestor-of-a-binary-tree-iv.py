# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes_vals = set([n.val for n in nodes])
        n_nodes = len(nodes_vals)

        def get_lca(node, lca, got_all):
            if node == None:
                return 0, lca
            
            if lca:
                return got_all, lca
            
            n_left, left_lca = get_lca(node.left, lca, got_all)

            if left_lca is not None:
                return got_all, left_lca
            
            n_right, right_lca = get_lca(node.right, lca, got_all)

            if right_lca is not None:
                return got_all, right_lca
            
            got_all = n_left + n_right

            if node.val in nodes_vals:
                got_all += 1
            
            if got_all == n_nodes:
                lca = node

            return got_all, lca

        _, lca = get_lca(root, None, 0)    
        return lca