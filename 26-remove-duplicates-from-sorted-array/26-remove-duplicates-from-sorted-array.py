class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        ret = 1
        for i in range(len(nums)-1):
            if nums[i+1] != nums[i]:
                ret += 1
                nums[ret-1] = nums[i+1]
        return ret
            
            
        