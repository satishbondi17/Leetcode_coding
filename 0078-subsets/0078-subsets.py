class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        tot = 1 << n
        res = []
        for num in range(tot):
            lst = []
            for i in range(n):
                if num & (1 << i):
                    lst.append(nums[i])
            res.append(lst)
        return res


        