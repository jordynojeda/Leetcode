class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        first_split = defaultdict(int)
        second_split = defaultdict(int)

        for number in nums:
            second_split[number] += 1
        
        for i in range(len(nums)):

            second_split[nums[i]] -= 1
            first_split[nums[i]] += 1

            if (first_split[nums[i]] * 2 > i + 1 and 
                second_split[nums[i]] * 2 > len(nums) - i - 1):
                return i
            
        return -1
