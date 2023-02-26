# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def nodeList(self, curNode, nodes):
        if curNode.left:
            self.nodeList(curNode.left, nodes)
        if curNode.right:
            nodes.append(curNode.val)
            self.nodeList(curNode.right, nodes)
            return
        nodes.append(curNode.val)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes=[]
        self.nodeList(root, nodes)
        for i in range(len(nodes)-1):
            if nodes[i]>=nodes[i+1]:
                return False
        return True