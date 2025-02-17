class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles) # char -> available count

        def backtrack():
            result = 0

            for char in count:
                if count[char] > 0:
                    count[char] -= 1
                    result += 1
                    result += backtrack()
                    count[char] += 1

            return result

        return backtrack()
