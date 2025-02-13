class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        result = 0
        heapq.heapify(nums)

        while nums[0] < k:
            number1 = heapq.heappop(nums)
            number2 = heapq.heappop(nums)

            new_number = number1 * 2 + number2

            heapq.heappush(nums, new_number)

            result += 1
        
        return result

