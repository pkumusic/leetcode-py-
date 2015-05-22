#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Filename: Solution.py
#COPYRIGHT@Music LEE
"""There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}

    # Solution 1 Start
    """
Solution #1. Easy Thought.
    1. Combine two arrays
    2. Calculate the median
    O((m+n)log(m+n))

    1,2,3 (3+1)/2  1,2,3,4 (4+1)/2 = 2.5
    Leetcode: Passed, 116ms (Strange, actually dont meet the O(log(m+n) criteria))
"""
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = nums1 + nums2
        nums3.sort()
        n = len(nums3)
        if n%2 == 0:
            return float((nums3[n/2-1]+nums3[n/2]))/2
        else:
            return nums3[(n+1)/2-1]

    # Solution 1 End

    # Solution 2 Start
    """ Two pointers
        O((m+n)/2)
        Intuitive one, just skip the implementation
"""
    # Solution 2 End

    # Solution 3 Start
    """
Solution #3. Interesting Thought.
    Extend this problem to find the kth small number in the two arrays
    Compare the k/2 th number in A and B
    1. if A[k/2-1] > B[k/2-1], than find the new k/2 small number in A,B[k/2-1:end]
    2. if equal, than A[k/2-1] is the number.
    O(log(m+n))

    1,2,3 (3+1)/2  1,2,3,4 (4+1)/2 = 2.5
    Leetcode: Passeds, 116ms (The data set is not good to test the result, but
    apparently this solution is much better)
"""
    def findKth(self, nums1, nums2, k):
        # make sure that len(nums1) less or equal than len(nums2)
        len1,len2 = len(nums1),len(nums2)
        if len1 > len2:
            return self.findKth(nums2, nums1, k)
        # Some bounding cases
        if len1 == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0],nums2[0])
        #divide k to two parts
        la = min(k/2,len1)
        lb = k-la
        if nums1[la-1]==nums2[lb-1]:
            return nums1[la-1]
        elif nums1[la-1] > nums2[lb-1]:
            return self.findKth(nums1, nums2[lb:], k-lb)
        else:
            return self.findKth(nums1[la:], nums2, k-la)
        
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1) + len(nums2)
        if n%2 == 0:
            return float(self.findKth(nums1, nums2, n/2)+self.findKth(nums1, nums2, n/2+1))/2
        else:
            return self.findKth(nums1, nums2, (n+1)/2)

    # Solution 3 End
        
        
        
        
    
        
        
                
        
                
                
            
                   
                    
            
        



