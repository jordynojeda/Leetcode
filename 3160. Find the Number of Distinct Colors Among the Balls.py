class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        result = []
        color_map = defaultdict(int)
        ball_map = defaultdict(int)

        for ball, color in queries:

            if ball in ball_map:
                
                previous_color = ball_map[ball]
                color_map[previous_color] -= 1

                if color_map[previous_color] == 0:
                    del color_map[previous_color]
                
            ball_map[ball] = color
            color_map[color] += 1

            result.append(len(color_map))
        
        return result
 
