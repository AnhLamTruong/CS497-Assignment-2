
from typing import Optional
class TreeNode: 
  def __init__(self , val): 
      self.value = val  
      self.left = None
      self.right = None
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    # Null node has 0 depth.
    if root == None:
      return 0

    # Get the depth of the left and right subtree 
    # using recursion.
    leftDepth = self.maxDepth(self,root.left)
    rightDepth = self.maxDepth(self,root.right)

    # Choose the larger one and add the root to it.
    if leftDepth > rightDepth:
      return leftDepth + 1
    else:
      return rightDepth + 1

# Driver code
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
# root.left.left = Node(4)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
#Input: root = [3,9,20,null,null,15,7]
print("The max depth is:", Solution.maxDepth(Solution,root))