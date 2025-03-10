class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def atleast_k(k):
            
            vowel = defaultdict(int)
            non_vowel = 0
            result = 0
            left = 0

            for right in range(len(word)):
                if word[right] in "aeiou":
                    vowel[word[right]] += 1
                else:
                    non_vowel += 1
                
                while len(vowel) == 5 and non_vowel >= k:
                    
                    result += (len(word) - right)

                    if word[left] in "aeiou":
                        vowel[word[left]] -= 1
                    else:
                        non_vowel -= 1
                    
                    if vowel[word[left]] == 0:
                        vowel.pop(word[left])

                    left += 1

            return result

        return atleast_k(k) - atleast_k(k + 1)
            
