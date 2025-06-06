class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            
            # Right half is sorted
            if nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            # Left half is sorted
            else:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                    
        return -1
