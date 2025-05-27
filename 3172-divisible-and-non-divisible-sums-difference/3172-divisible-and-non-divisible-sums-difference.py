class Solution(object):
    def differenceOfSums(self, n, m):
        sum=0
        non_div=0
        for i in range(1,n+1):
            if i%m==0:
              non_div+=i
            else:
                sum+=i
        return sum-non_div
    
       
        