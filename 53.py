class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curs=maxs=nums[0]
        for num in nums[1: ]:
            curs=max(num,curs+num)
            maxs=max(curs,maxs)
            
        return maxs