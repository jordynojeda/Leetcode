class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        result = []

        for i in range(2):
            for number in nums:
                result.append(number)
        
        return result
