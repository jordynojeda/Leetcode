class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        stack = []
        part_length = len(part)

        for char in s:

            stack.append(char)

            if len(stack) >= part_length and self.check_match(stack, part, part_length):
                for _ in range(part_length):
                    stack.pop()

        return "".join(stack)

    
    def check_match(self, stack, part, part_length) -> bool:
        # Get the last 'part_length' elements from 'stack'
        last_elements = stack[-part_length:]
        
        # Join these elements into a single string
        last_elements_str = "".join(last_elements)
        
        # Compare the resulting string with 'part'
        is_match = last_elements_str == part
        
        # Return the result of the comparison
        return is_match
