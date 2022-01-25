class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort(key=lambda x: len(x)) 
        if len(strs)==0:
            return ""
        else:
            for i in range(len(strs[0])):
                for j in range(len(strs)-1):
                    if strs[0][i] != strs[j+1][i]:
                        return strs[0][:i]
            return strs[0]