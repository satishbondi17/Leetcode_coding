#Python SOlution
class Solution(object):
    def minElement(self, nums):
       
        ans = float('inf')
        for num in nums:
            ans = min(ans, sum(ord(x) - ord('0') for x in str(num)))
        return ans

        