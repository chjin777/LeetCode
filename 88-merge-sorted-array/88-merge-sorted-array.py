class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums2.sort()
            for i in range(0, n):
                nums1[i] = nums2[i]
        elif n == 0:
            nums1.sort()
        else:
            for i in range(0, (len(nums1) - m)):
                nums1.pop()
            for i in range(0, n):
                nums1.append(nums2[i])
            nums1.sort()