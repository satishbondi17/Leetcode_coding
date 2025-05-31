class Solution(object):
    def kthSmallest(self, matrix, k):
        flat = [num for row in matrix for num in row]
        flat.sort()
        for i in range(0,len(flat)):
            if i==k-1:
                return flat[i]
        return 0
        