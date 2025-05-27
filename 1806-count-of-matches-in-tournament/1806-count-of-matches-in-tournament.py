class Solution(object):
    def numberOfMatches(self, n):
        current = 0
        while n > 1:
            if n % 2 == 0:
                current += n // 2
                n = n // 2
            else:
                current += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return current
