class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)

        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            
            dp_next = set()
            
            for t in dp:
                if t + nums[i] == target:
                    return True
                    
                dp_next.add(t + nums[i])
                dp_next.add(t)
            
            dp = dp_next

        return True if target in dp else False

