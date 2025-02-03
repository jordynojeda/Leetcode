class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        current = 1
        result = 1
        increasing = 0

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                if increasing > 0:
                    current += 1
                else:
                    current = 2
                    increasing = 1

            elif nums[i-1] > nums[i]:
                if increasing < 0:
                    current += 1
                else:
                    current = 2
                    increasing = -1

            else:
                current = 1
                increasing = 0

            result = max(result, current)

        return result
