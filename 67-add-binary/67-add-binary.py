class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ret = int('0b'+a, 2) + int('0b'+b, 2)
        return format(int('0b'+a, 2) + int('0b'+b, 2), 'b')
        