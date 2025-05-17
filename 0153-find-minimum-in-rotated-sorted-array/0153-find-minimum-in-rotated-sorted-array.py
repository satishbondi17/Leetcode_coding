class Solution(object):
    def findMin(self, nums):
        n=len(nums)
        low,high=0,n-1
        mini=float("inf")
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=nums[high]:
                mini=min(mini,nums[mid])
                high=mid-1
            else:
                mini=min(mini,nums[low])
                low+=1
        return mini
        