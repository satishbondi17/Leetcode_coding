class Solution(object):
    def searchRange(self, nums, target):
        start = -1
        end = -1
        for i in range(len(nums)):
          #  for j in range(i+1,len(nums)):
          if nums[i]==target:
            
            if start == -1:
                start = i
            end = i
        return [start, end]
