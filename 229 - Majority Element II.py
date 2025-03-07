class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        result = []
        count = defaultdict(int)
        
        for n in nums:
            count[n] += 1

            if len(count) <= 2:
                continue
            
            new_count = defaultdict(int)
            for key, val in count.items():
                if val > 1:
                    new_count[key] = val - 1
                
            count = new_count

        result = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                result.append(n)

        return result
            


