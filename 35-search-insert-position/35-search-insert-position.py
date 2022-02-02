class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] > target:
            return 0
        if nums[-1] == target:
            return len(nums)-1
        if nums[-1] < target:
            return len(nums)
        for i in range(len(nums)-1):
            if nums[i] == target: 
                return i
            if nums[i] < target < nums[i+1]:
                return i+1