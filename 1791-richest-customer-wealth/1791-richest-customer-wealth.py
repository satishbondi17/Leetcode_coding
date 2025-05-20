class Solution(object):
    def maximumWealth(self, accounts):
        
        max_sum=0
       
      
        for i in accounts:
            count=sum(i)
            if count>max_sum:
                max_sum=count

        return max_sum

       
        