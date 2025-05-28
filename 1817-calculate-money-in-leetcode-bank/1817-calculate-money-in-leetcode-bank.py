class Solution(object):
    def totalMoney(self, n):
        total = 0
        for day in range(n):
            total += (day // 7 + 1) + (day % 7)
        
        return total