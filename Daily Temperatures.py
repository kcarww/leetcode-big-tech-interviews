'''
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Using monotonic stack for this solution
'''
class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = [0] * len(temperatures)
        stack = []
        for currDay, currTemp in enumerate(temperatures):
            while stack and currTemp > temperatures[stack[-1]]:
                lastDay = stack.pop()
                n[lastDay] = currDay - lastDay
            stack.append(currDay)
        return n
