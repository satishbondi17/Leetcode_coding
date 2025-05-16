class Solution(object):
    def oddCells(self, m, n, indices):
        row = [0] * m
        col = [0] * n

        for r, c in indices:
            row[r] += 1
            col[c] += 1

        odd_count = 0
        for i in range(m):
            for j in range(n):
                if (row[i] + col[j]) % 2 != 0:
                    odd_count += 1

        return odd_count


        
    
        