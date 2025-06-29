class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        mod = 10**9 + 7
        left, right = 0, len(nums) - 1

        # Precompute powers of 2 up to len(nums)
        pow2 = [1] * (len(nums))
        for i in range(1, len(nums)):
            pow2[i] = pow2[i - 1] * 2 % mod

        result = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                result += pow2[right - left]
                result %= mod
                left += 1
            else:
                right -= 1

        return result

        