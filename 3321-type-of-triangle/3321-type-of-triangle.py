class Solution(object):
    def triangleType(self, nums):
        nums.sort()
        a,b,c=nums[0],nums[1],nums[2]
        if a+b<=c:
            return "none"
        if a==b and b==c and c==a:
            return "equilateral"
        elif a==b or b==c or c==a:
            return "isosceles"
        else:
            return "scalene"
        