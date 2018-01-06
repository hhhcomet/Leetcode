class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        l=1
        
        for i in xrange(1,len(nums)):
            if nums[l-1]!=nums[i]:
                l+=1
                nums[l-1]=nums[i]
        
        return l