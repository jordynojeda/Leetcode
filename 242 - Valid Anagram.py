class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = defaultdict(int)

        for letter in t:
            count[letter] += 1

        for letter in s:
            count[letter] -= 1

        for value in count.values():
            if value != 0:
                return False
        
        return True
