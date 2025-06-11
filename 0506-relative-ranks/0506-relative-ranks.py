class Solution(object):
    def findRelativeRanks(self, score):
        # Step 1: Sort scores in descending order and keep track of original indices
        sorted_scores = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        
        # Step 2: Assign ranks
        result = [''] * len(score)
        for rank, (s, i) in enumerate(sorted_scores):
            if rank == 0:
                result[i] = "Gold Medal"
            elif rank == 1:
                result[i] = "Silver Medal"
            elif rank == 2:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank + 1)
        
        return result
