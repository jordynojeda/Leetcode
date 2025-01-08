class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        result = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    result += 1

        return result
                
    def isPrefixAndSuffix(self, str1, str2):

        if not str2.startswith(str1):
            return False

        if not str2.endswith(str1):
            return False

        return True
