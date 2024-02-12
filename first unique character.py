# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution(object):
    def firstUniqChar(self, s: str) -> int:
        arr = [0 for i in range(26)]
        for letra in s:
            arr[ord(letra) - 97] += 1

        for i in range(len(s)):
            if arr[ord(s[i]) - 97] == 1:
                return i

        return -1
