class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        result = 0
        
        current = 0 # bitmask
        left = 0

        for right in range(len(nums)):

            while current & nums[right]:
                current = current ^ nums[left]
                left += 1
            
            result = max(result, right - left + 1)
            current |= nums[right]

        return result
