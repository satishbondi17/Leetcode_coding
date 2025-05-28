class Solution(object):
    def minimumSum(self, num):
        digits = list(map(int, str(num)))
        digits.sort()
        # Distribute digits alternately
        new1 = digits[0] * 10 + digits[2]
        new2 = digits[1] * 10 + digits[3]
        return new1 + new2

        