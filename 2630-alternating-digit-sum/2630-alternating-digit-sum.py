class Solution(object):
    def alternateDigitSum(self, n):
        count=0
        digits = list(map(int, str(n))) 
        for i,digit in  enumerate(digits):
            rem=n%10
            if i%2==0:
                count+=digit
            else:
                count-=digit
        return count

        