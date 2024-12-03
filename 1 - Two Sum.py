class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        complement = defaultdict(int)

        for idx, number in enumerate(nums):
            if (target - number) in complement:
                result.append(complement[target - number])
                result.append(idx)
                break

            complement[number] = idx

        return result
