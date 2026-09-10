# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
        arr = [] 

        while temp:
            arr.append(temp)
            temp = temp.next 

        mid = len(arr)//2 

        return arr[mid]    



