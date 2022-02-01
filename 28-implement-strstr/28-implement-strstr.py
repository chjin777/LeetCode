class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        if haystack==needle:
            return 0
        for i in range(len(haystack)-1+1):
            if haystack[i:i+l]==needle:
                return i 
        return -1
        