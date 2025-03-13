class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        lenght = len(nums)
        left, right = 0, len(queries)

        if not self.zeros_array(nums, queries, right):
            return -1

        while left <= right:
            mid = (left + right) // 2
            if self.zeros_array(nums, queries, mid):
                right = mid -1
            else:
                left = mid + 1
        
        return left

    def zeros_array(self, nums, queries, k):
        total_sum = 0
        difference_array = [0] * (len(nums) + 1)

        for query_index in range(k):
            start, end, value = queries[query_index]

            difference_array[start] += value
            difference_array[end + 1] -= value

        for i in range(len(nums)):
            total_sum += difference_array[i]
            if total_sum < nums[i]:
                return False
        
        return True
