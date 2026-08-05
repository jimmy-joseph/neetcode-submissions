# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = list1, list2

        dummy = ListNode()

        if not head1:
            if head2:
                return head2
            return
        
        if not head2:
            if head1:
                return head1
            return

        tail = dummy            
       
        while head1 and head2:
            print(head1.val)
            print(head2.val)
            if head1.val > head2.val:
                tail.next = head2
                head2 = head2.next
            else:
                tail.next = head1
                head1 = head1.next
            
            tail = tail.next
        
        while head1:
            tail.next = head1
            head1 = head1.next
            tail = tail.next

        while head2:
            tail.next = head2
            head2 = head2.next
            tail = tail.next

        return dummy.next