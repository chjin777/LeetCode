class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {'}':'{',')':'(',']':'['}
        stack = []
        for i in s:
            if i in pairs:
                if len(stack)!=0 and stack[-1] == pairs[i]: #len(stack)!=0 and 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if len(stack)!=0:
            return False
        return True