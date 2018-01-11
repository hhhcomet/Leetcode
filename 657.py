class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        start=[0,0]
        dir={'R':(0,1),'U':(1,0),'L':(0,-1),'D':(-1,0)}
        for i in range(len(moves)):
            start[1]+=dir[moves[i]][1]
            start[0]+=dir[moves[i]][0]
        if start==[0,0]:
            return True
        else:
            return False
        