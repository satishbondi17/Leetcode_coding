class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        sum=arrivalTime+delayedTime
        
        return sum % 24
        