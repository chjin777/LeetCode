class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        maxlist = [nums[0]]
        for i in range(1,len(nums)):
            ret = max(ret + nums[i], nums[i])
            maxlist.append(ret)
        return max(maxlist)
    ##kadene's algorithm