class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        mi= triangle[-1]
        for i in xrange(len(triangle)-2,-1,-1):
            for j in xrange(len(triangle[i])):
                mi[j]=min(mi[j],mi[j+1])+triangle[i][j]
                            
                 
        
       
        return mi[0]