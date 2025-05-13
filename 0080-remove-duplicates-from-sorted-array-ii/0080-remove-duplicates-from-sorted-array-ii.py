class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        
        i = 2  # Start from index 2 since the first two elements are always allowed
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:  # Compare with the element 2 places before
                nums[i] = nums[j]
                i += 1
        return i


        
        