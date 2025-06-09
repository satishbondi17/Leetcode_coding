class Solution(object):
    def findTheWinner(self, n, k):
        count=0
        for i in range(1,n+1):
            count=(count+k)%i
        return count+1
        