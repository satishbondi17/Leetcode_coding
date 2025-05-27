class Solution(object):
    def canWinNim(self, n):
        res=n%4
        if res!=0:
            return True
        return False
        