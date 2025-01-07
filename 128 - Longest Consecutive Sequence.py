class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        result = 0

        for number in nums:
            # Check if it's the start of a sequence
            if (number - 1) not in nums_set:
                length = 1
                while (number + length) in nums_set:
                    length += 1
                result = max(result, length)

        return result
