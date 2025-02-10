class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        result = 0
        count = 0

        for number in nums:

            if count == 0:
                count += 1
                result = number
            elif result == number:
                count += 1
            else:
                count -= 1
        
        return result
