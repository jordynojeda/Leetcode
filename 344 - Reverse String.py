class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left  = 0
        right = len(s) - 1

        while left <= right:

            left_character = s[left]
            right_character = s[right]

            s[left] = right_character
            s[right] = left_character
        
            left += 1
            right -= 1
        
