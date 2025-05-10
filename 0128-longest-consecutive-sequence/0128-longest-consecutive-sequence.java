import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;

        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);  // Add all numbers to a set for quick lookup
        }

        int longestStreak = 0;

        for (int num : numSet) {
            // Start counting only if it's the beginning of a sequence
            if (!numSet.contains(num - 1)) {  
                int currentNum = num;
                int currentStreak = 1;

                // Check how long the streak is
                while (numSet.contains(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }

                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
}
