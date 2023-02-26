# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.visited=[]

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curNode=root

        if curNode==None:
            return 

        self.visited.append(curNode.val)
        if curNode.left:
            childNode=curNode.left
            self.preorderTraversal(childNode)
        if curNode.right:
            childNode=curNode.right
            self.preorderTraversal(childNode)

        return self.visited
        