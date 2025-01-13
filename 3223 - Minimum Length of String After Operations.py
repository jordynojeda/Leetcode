class Solution:
    def minimumLength(self, s: str) -> int:
        
        result = 0
        character_count = defaultdict(int)
        
        for character in s:
            character_count[character] += 1
        
        for character, count in character_count.items():

            if count % 2 == 0:
                result += 2
            else:
                result += 1

        return result
