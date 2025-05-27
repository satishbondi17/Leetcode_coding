class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)  # sort in descending order
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if a < b + c:  # triangle condition
                return a + b + c
        return 0  # no valid triangle found



        
        