# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
         l_list = [] 
         curr = head 

         while curr:
            l_list.append(curr.val)     
            curr = curr.next

         reverse = l_list[::-1]    
         if  reverse == l_list:
            return True 
         else :
           return False    
        