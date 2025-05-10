class Solution(object):
    def isPalindrome(self, x):
        res=0
        num=x
        while x>0:
            rem=x%10
            res=(res*10)+rem
            x=x//10
        return num==res
        
        