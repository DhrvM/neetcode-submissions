class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = nums.count(0)
        w = nums.count(1)
        b = nums.count(2)

        for i in range(len(nums)):
            if i < r:
                nums[i] = 0
            elif i < r + w:
                nums[i] = 1
            else:
                nums[i] = 2











"""
Naive is any sorting algorithm

[0, 1, 2, 0, 2, 2, 1]
l = 0
r = 0


O(n)
r, w, b = count(nums, 0), count(nums, 1), count (nums, 2)
for i in nums.indexes:
    nums[i] = r
"""