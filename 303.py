class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr=nums;
        for i in xrange(1,len(nums)):
            self.arr[i] +=self.arr[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.arr[j]-(self.arr[i-1] if i>0 else 0)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)