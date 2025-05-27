class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        
        count = 1 
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                count += i
                if i != num // i:
                    count += num // i
        return count == num

       
        