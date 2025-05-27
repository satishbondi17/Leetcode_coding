class Solution(object):
    def pivotInteger(self, n):
        tot=n*(n+1)//2
        count=0
        for i in range(1,n+1):
            count+=i
            if count==tot-count+i:
                return i
        return -1



        