#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Filename: Solution.py
#COPYRIGHT@Music LEE
"""Given a string, find the length of the longest substring without repeating
characters. For example, the longest substring without repeating letters for
"abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring
is "b", with the length of 1.
"""

class Solution:
    # @param {string} s
    # @return {integer}
    # Solution 1 Start
    """
    Observe: if a substring of length n is not found,a substring of n+1 can not be found
    Idea 1 Brute-Force
    for n = 1 to length:
        if a substring can be found of length n
           (use a set to judge)  O(n^2)
        flag = n
        continue, until can't be found, break.
    Overall: About O(n^3)
    LeetCode: Time Out
    """
    def lengthOfLongestSubstring(self, s):
        flag = 1
        for i in range(1,len(s)+1):
            if self.findSubstring(s,i):
                flag = i
            else:
                break
        return flag

    def findSubstring(self,s,sub_length):
        """Find if a length i no repeating substring can be found in s,
Example:
'abcde' , length = 5, sub_length = 3
abc,bcd,cde  index from 0 to 2
"""
        length = len(s)
        if length < sub_length:
            return False
        for i in range(length-sub_length+1):
            if self.noRepeating(s[i:i+sub_length]):
                return True
            pass
        return False

    def noRepeating(self,s):
        p = {}
        for i in range(len(s)):
            if s[i] in p:
                return False
            p[s[i]]=s[i]
        return True
    # Solution 1 End

    # Solution 2 Start
    def lengthOfLongestSubstring(self, s):
        """
    Actually we only need two pointers i and j to find the substring
    1. first set i fixed. move j rightward until the string have repeated items.
    2. then fix j, move i rightward until there is no repeated items.
    3. Repeat 1,2. Store all the possible length.
    4. return the max length

    Time Complexity:O(n)
    Leetcode: Passed (108ms)
    """
        i=j=0
        maxlength = 0
        n = len(s)
        exist = {}
        while(i<n and j<n):
            if s[j] not in exist:
                exist[s[j]]=1109 # Whatever value
                j += 1
                maxlength = max(maxlength,j-i)
            else:               
                while(s[i]!=s[j]):
                    del exist[s[i]]
                    i += 1
                i += 1
                j += 1
        return maxlength                       
    # Solution 2 End
            
            
        
        
                
        
                
                
            
                   
                    
            
        



