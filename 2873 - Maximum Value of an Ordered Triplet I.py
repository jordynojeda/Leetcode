class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        result = 0
        left = nums[0]

        for j in range(1, len(nums)):
            if nums[j] > left:
                left = nums[j]
                continue 
            for k in range(j + 1, len(nums)):
                result = max(result, (left - nums[j]) * nums[k])

        return result
