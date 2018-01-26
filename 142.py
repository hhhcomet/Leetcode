# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visit=set()
        cur=head
        while cur is not None:
            if cur in visit:
                return cur
            else:
                visit.add(cur)
                cur=cur.next
        
        return None