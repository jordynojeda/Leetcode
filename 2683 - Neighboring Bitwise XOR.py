class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        result = 0

        for bit in derived:
            result ^= bit
        
        return True if result == 0 else False
