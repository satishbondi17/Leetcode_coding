class Solution(object):
    def countNegatives(self, grid):
        m=len(grid)
        n=len(grid[0])
        col=n-1
        row=0
        count=0
        while row<m and col>=0:
            if grid[row][col]<0:
                count+=m-row
                col-=1
            else:
                row+=1
        return count
                
       


        
        return count

        