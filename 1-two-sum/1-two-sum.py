class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        for i in range(len(nums)-1):
            sec = target - nums[i]
            if sec in nums[i+1:]:
                ret.append(i)
                ret.append(nums[i+1:].index(sec)+i+1)
                break
        return ret
            
        