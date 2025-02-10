class Solution:
    def clearDigits(self, s: str) -> str:
        
        result = ""
        removal_count = 0

        for i in range(len(s) - 1, -1, -1):

            if s[i].isdigit():
                removal_count += 1
            elif removal_count and not s[i].isdigit():
                removal_count -= 1
            else:
                result += s[i]

        return result[::-1]
