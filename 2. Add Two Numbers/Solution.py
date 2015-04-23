# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
       self.val = x
       self.next = None

       

"""
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Complexity Analysis: O(max(m,n))
"""
class Solution:
    """
My raw solution: 160ms
"""
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode(0)
        l_temp = l3
        flag = 0 # recording for carry
        l1dig , l2dig = l1.val , l2.val
        while(True):
  
            val_l3 = l1dig + l2dig + flag
            if val_l3 > 9:
                val_l3 -= 10
                flag = 1
            else:
                flag = 0
                
            l_temp.val = val_l3

            if(l1 is None):
                l1dig = 0
            elif(l1.next is None):
                l1dig, l1 = 0, None
            else:
                l1 = l1.next
                l1dig = l1.val

            if(l2 is None):
                l2dig = 0
            elif(l2.next is None):
                l2dig, l2 = 0, None
            else:
                l2 = l2.next
                l2dig = l2.val
            
            if(l1 is None and l2 is None and flag is 0):
                return l3
            else:
                l_temp.next = ListNode(0)
                l_temp = l_temp.next



class Solution:
    """a more succint soluiton:220ms
"""
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        sum = ListNode(0)
        s = sum
        while l1 is not None or l2 is not None or carry:
            s.val = carry
            if l1:
                s.val += l1.val
                l1 = l1.next
            if l2:
                s.val += l2.val
                l2 = l2.next
            carry = s.val / 10
            s.val = s.val % 10
            if l1 or l2 or carry:
                s.next = ListNode(0)
                s = s.next
        return sum


            
            
            
            
            
            
