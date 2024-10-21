class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_index = defaultdict(int)
        result = []

        for i in range(len(s)):
            last_index[s[i]] = i
        
        size = 0
        end = 0
        for i in range(len(s)):
            
            size += 1
            end = max(end, last_index[s[i]])

            if i == end:
                result.append(size)
                size = 0

        return result
