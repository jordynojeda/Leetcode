class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        result = 0
        distinct_numbers_greater_k = set()

        for number in nums:
            if number < k:
                return -1
            elif number > k and number not in distinct_numbers_greater_k:
                distinct_numbers_greater_k.add(number)
                result += 1

        return result
