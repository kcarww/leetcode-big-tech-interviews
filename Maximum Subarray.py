# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        currentSubArray = maxSubArray = nums[0]
        for num in nums[1:]:
            currentSubArray = max(num, currentSubArray + num)
            maxSubArray = max(maxSubArray, currentSubArray)
        return maxSubArray
