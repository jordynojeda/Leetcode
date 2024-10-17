class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        good_positions = set()

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            for index, value in enumerate(triplet):
                if value == target[index]:
                    good_positions.add(index)
        
        return len(good_positions) == len(target)
