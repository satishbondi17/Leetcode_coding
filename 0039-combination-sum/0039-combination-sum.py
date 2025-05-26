class Solution(object):
    def solve(self, index, tot, subset, nums, target, res):
        if tot == target:
            res.append(subset[:])
            return
        if tot > target or index >= len(nums):
            return

        # Include nums[index]
        subset.append(nums[index])
        self.solve(index, tot + nums[index], subset, nums, target, res)  # reuse allowed
        subset.pop()

        # Exclude nums[index] and move to next
        self.solve(index + 1, tot, subset, nums, target, res)

    def combinationSum(self, candidates, target):
        res = []
        self.solve(0, 0, [], candidates, target, res)
        return res
