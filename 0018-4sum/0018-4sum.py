class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        ans = []
        nums.sort()
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, n - 1
                while k < l:
                    tot = nums[i] + nums[j] + nums[k] + nums[l]
                    if tot == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif tot < target:
                        k += 1
                    else:
                        l -= 1
        return ans
