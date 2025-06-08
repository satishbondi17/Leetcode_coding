class Solution(object):
    def lexicalOrder(self, n):
        result = []
        curr = 1
        for _ in range(n):
            result.append(curr)
            if curr * 10 <= n:
                curr *= 10  # go deeper
            elif curr % 10 != 9 and curr + 1 <= n:
                curr += 1  # go to next sibling
            else:
                while (curr // 10) % 10 == 9:
                    curr //= 10  # backtrack up until you find a sibling
                curr = curr // 10 + 1  # go to next sibling of parent
        return result
