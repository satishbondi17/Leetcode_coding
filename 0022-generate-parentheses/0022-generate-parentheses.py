class Solution(object):
    def generateParenthesis(self, n):
        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                res.append(current)
                return

            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        res = []
        backtrack("", 0, 0)
        return res
