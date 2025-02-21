# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.bfs(root)
        
    def find(self, target: int) -> bool:
        return target in self.seen

    def bfs(self, root):
        queue = [root]
        root.val = 0

        while queue:
            current_node = queue.pop(0)

            self.seen.add(current_node.val)
            if current_node.left:
                current_node.left.val = current_node.val * 2 + 1
                queue.append(current_node.left)
            if current_node.right:
                current_node.right.val = current_node.val * 2 + 2
                queue.append(current_node.right)
