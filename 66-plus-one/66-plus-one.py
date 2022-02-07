class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i]*(10**(len(digits)-i-1))
        num +=1
        ret = [int(a) for a in str(num)]
        return ret
    
        