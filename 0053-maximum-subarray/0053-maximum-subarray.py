class Solution(object):
    def maxSubArray(self, nums):
        max_sum = float("-inf")
        tot =0

        for i in range(0,len(nums)):
            tot += nums[i]
            max_sum = max(max_sum, tot)
            if tot< 0:
                tot = 0

        return max_sum


        