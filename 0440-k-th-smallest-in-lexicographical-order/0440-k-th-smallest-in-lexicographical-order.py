class Solution(object):
    def findKthNumber(self, n, k):
        def calc_steps(prefix, n):
            steps = 0
            first = prefix
            last = prefix
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps

        curr = 1
        k -= 1  # because we start from 1

        while k > 0:
            steps = calc_steps(curr, n)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr

        