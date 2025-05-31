class Solution(object):
    def findDuplicates(self, nums):
        res = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                res.append(abs(num))
            else:
                nums[index] *= -1
        return res
