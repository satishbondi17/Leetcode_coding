class Solution(object):
    def isPowerOfFour(self, n):
        if n<1:
            return False
        while n%4==0:
            n/=4
        return n==1