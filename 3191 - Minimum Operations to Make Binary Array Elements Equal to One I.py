class Solution:
    def minOperations(self, nums: List[int]) -> int:

        def flip(nums, i):
            nums[i] = 0 if nums[i] else 1
        
        result = 0
        for i in range(len(nums) - 2):

            if nums[i] == 0:
                flip(nums, i)
                flip(nums, i + 1)
                flip(nums, i + 2)
                result += 1

        if not nums[-1] or not nums[-2]:
            result = -1
        
        return result

