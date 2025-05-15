class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        
        res = []
        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse top row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            # Traverse right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            # Traverse bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            # Traverse left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res
