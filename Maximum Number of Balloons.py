'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
'''


class Solution(object):
    def maxNumberOfBalloons(self, text):
        charCount = {}
        balloonCount = 0
        for i in text:
            if i in charCount:
                charCount[i] += 1
            else:
                charCount[i] = 1
        while (charCount.get('b', 0) > 0
                and charCount.get('a', 0) > 0
                and charCount.get('l', 0) > 1
                and charCount.get('o', 0) > 1
                and charCount.get('n', 0) > 0):
            balloonCount += 1
            charCount['b'] -= 1
            charCount['a'] -= 1
            charCount['l'] -= 2
            charCount['o'] -= 2
            charCount['n'] -= 1

        return balloonCount
