'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

class Solution(object):
    def longestConsecutive(self, nums):
        setNums = set(nums)
        maxCount = 0
        for num in setNums:
            if num - 1 not in setNums:
                count = 1
                currentNum = num + 1
                while currentNum in setNums:
                    count += 1
                    currentNum += 1
                maxCount = max(maxCount, count)
        return maxCount
