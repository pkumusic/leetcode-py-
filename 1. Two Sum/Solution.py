#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Filename:
#COPYRIGHT@Music LEE
"""Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. 
Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""
class Solution:
    # @return a tuple, (index1, index2)where index1 < index2
    """BIdea 1: Brute-Force
	Keeping the array unsorted.
	Iterate the total array. In each iteration, iterate the array and find the remaining number.
	Complexity Analysis: O(n^2) in worst case
	Leetcode Result: Time out"""
    def twoSum(self, num, target):
        remain = map(lambda x: target-x, num)
        for i in num:
            if i in remain:
                return (num.index(i), remain.index(target-i))

class Solution2:
    # @return a tuple, (index1, index2)where index1 < index2
    """Idea 2: Hash map
	Add all the integers in the array to a hash map. O(n) 
	（Actually we don't need this pre-process. we can add the element while in the searching operation）
	Iterate the total array. In each iteration, calculate the remaining integer and searching the integer 
	in the hash map. 
	
	Complexity Analysis: O(n) time, O(n) space if the search operation in Hash map is O(1)
	Leetcode Result: Passed"""
    def twoSum(self, num, target):
        process={} #dict is a hashmap
        for index in range(len(num)):
            if target-num[index] in process:
                return [process[target-num[index]]+1,index+1]
            process[num[index]]=index

            
"""		
Idea 3: Sort and Binary Search
	1.Sort the numbers.O(nlogn)
	2.Iteration the numbers and use binary search to find the remaining. O(nlogn)
 	
 	Complexity Analysis: O(nlogn)
 	Leetcode Result: Passed
 *
 */
"""


