# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeNodes(self, head):
        head = head.next
        if not head:
            return head

        temp = head
        temp_sum = 0
        while temp.val != 0:
            temp_sum += temp.val
            temp = temp.next
        
        head.val = temp_sum
        head.next = self.mergeNodes(temp)
        return head