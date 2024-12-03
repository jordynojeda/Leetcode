class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()

        for number in nums:
            if number in duplicates:
                return True
            duplicates.add(number)

        return False
