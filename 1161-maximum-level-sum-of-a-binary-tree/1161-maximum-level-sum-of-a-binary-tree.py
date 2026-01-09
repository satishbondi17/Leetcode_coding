from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        queue = deque([root])
        level = 1
        max_sum = float('-inf')
        result = 1

        while queue:
            curr_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                curr_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if curr_sum > max_sum:
                max_sum = curr_sum
                result = level

            level += 1

        return result
