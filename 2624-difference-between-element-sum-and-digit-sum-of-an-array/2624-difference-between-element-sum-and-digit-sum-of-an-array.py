class Solution(object):
    def differenceOfSum(self, nums):
        element_sum = sum(nums)
        digit_sum = sum(int(digit) for num in nums for digit in str(num))
        return abs(element_sum - digit_sum)
