class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0:
            return []
        l=[[0 for i in range(n)] for i in range(n)]
        cnt=0
        x=0
        y=0 
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        
        for i in range(n*n):
            l[x][y]=i+1
            dx,dy=dir[cnt%4]
            if -1<x+dx<n and -1<y+dy<n and l[x+dx][y+dy]==0:
                x=x+dx
                y=y+dy
            else:
                cnt+=1
                dx,dy=dir[cnt%4]
                x,y=x+dx,y+dy
            

        return l