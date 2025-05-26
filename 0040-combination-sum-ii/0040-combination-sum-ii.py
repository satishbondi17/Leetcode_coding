class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def backtrack(start, remain, path):
            if remain == 0:
                res.append(list(path))
                return
            for i in range(start, len(candidates)):
                # skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                backtrack(i + 1, remain - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return res

        