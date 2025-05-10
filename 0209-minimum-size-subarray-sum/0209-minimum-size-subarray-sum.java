class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int min_value=Integer.MAX_VALUE;
        int i=0;
        int j=0;
        int curr_sum=0;
        for(j=0;j<nums.length;j++){
            curr_sum+=nums[j];
            while(curr_sum>=target){
                if(j-i+1<min_value){
                    min_value=j-i+1;

                }
                curr_sum-=nums[i];
                i++;
            }
        }
        return min_value!=Integer.MAX_VALUE ? min_value:0;
    }
}