class Solution(object):
    def maxSubsequence(self, nums, k):
        # Step 1: Pair each element with its index
        indexed_nums = list(enumerate(nums))
        
        # Step 2: Sort by value, and take top k largest elements
        top_k = sorted(indexed_nums, key=lambda x: x[1], reverse=True)[:k]
        
        # Step 3: Sort the selected elements by original index to maintain order
        top_k_sorted = sorted(top_k, key=lambda x: x[0])
        
        # Step 4: Extract the values
        return [num for idx, num in top_k_sorted]
