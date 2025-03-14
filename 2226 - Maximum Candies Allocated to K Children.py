class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        total = sum(candies)

        if total < k:
            return 0

        left, right = 1, total // k
        result = 0

        while left <= right:
            mid = (left + right) // 2
            count = 0

            for candy in candies:
                if candy >= mid:
                    count += candy // mid
            
            if count >= k:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result
        
