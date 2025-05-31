class Solution(object):
    def kthSmallest(self, matrix, k):
        flat = [num for row in matrix for num in row]
        flat.sort()
        return flat[k - 1]
