class Solution(object):
    def missingNumber(self, nums):

        n=len(nums)
        tot=(n*(n+1))//2
        sum=0
        for i in range(0,n):
            sum+=nums[i]
        return tot-sum
        


        