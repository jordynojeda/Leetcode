class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = []

        left_word1 = 0
        left_word2 = 0

        while left_word1 < len(word1) and left_word2 < len(word2):

            result.append(word1[left_word1])
            result.append(word2[left_word2])

            left_word1 += 1
            left_word2 += 1
        
        if left_word1 < len(word1):
            result.append(word1[left_word1:len(word1)])

        if left_word2 < len(word2):
            result.append(word2[left_word2:len(word2)])

        return "".join(result)
