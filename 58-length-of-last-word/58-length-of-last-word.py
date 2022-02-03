class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.strip()
        if " " not in new:
            return len(new)
        for i in range(1, len(new)+1):
            if new[-i]==" ":
                return i-1