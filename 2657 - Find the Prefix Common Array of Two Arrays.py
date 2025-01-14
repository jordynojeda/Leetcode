class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        result = []

        frequency = defaultdict(int)
        numbers_in_common = 0

        for i in range(len(A)):

            frequency[A[i]] += 1
            if frequency[A[i]] == 2:
                numbers_in_common += 1

            frequency[B[i]] += 1
            if frequency[B[i]] == 2:
                numbers_in_common += 1
            
            result.append(numbers_in_common)
        
        return result
        
