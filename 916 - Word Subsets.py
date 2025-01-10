class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        count_2 = defaultdict(int)

        for word in words2:
            count_w = Counter(word)
            for character, count in count_w.items():
                count_2[character] = max(count_2[character], count)

        result = []

        for word in words1:
            count_w = Counter(word)
            flag = True

            for character, count in count_2.items():
                if count_w[character] < count:
                    flag = False
                    break

            if flag:
                result.append(word)

        return result
