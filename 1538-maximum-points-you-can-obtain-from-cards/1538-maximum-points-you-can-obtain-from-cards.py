class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        total = sum(cardPoints[:k])
        max_score = total

        for i in range(1, k + 1):
            total = total - cardPoints[k - i] + cardPoints[-i]
            max_score = max(max_score, total)

        return max_score
        