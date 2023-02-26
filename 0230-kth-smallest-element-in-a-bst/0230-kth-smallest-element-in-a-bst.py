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
        
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curNode=root
        nodes=[]
        self.nodeList(curNode, nodes)
        return nodes[k-1]