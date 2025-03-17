class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        odd_set= set()

        for number in nums:
            if number not in odd_set:
                odd_set.add(number)
            else:
                odd_set.remove(number)

        return len(odd_set) == 0 
