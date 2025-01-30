class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def get_connected_component(src):
            queue = deque([src]) 
            component = set([src])       

            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if neighbor in component:
                        continue
                    queue.append(neighbor)
                    component.add(neighbor)
                    visit.add(neighbor)

            return component

        def longest_path(src):
            queue = deque([(src, 1)])   # (node, group)
            distance = {src: 1}         # node -> length from src + 1

            while queue:
                node, length = queue.popleft()
                for neighbor in adj[node]:
                    if neighbor in distance:
                        if distance[neighbor] == length:
                            return -1
                        continue
                    queue.append((neighbor, length + 1))
                    distance[neighbor] = length + 1

            return max(distance.values())
        
        visit = set()
        result = 0
        for i in range(1, n + 1):
            if i in visit:
                continue 
            
            visit.add(i)
            component = get_connected_component(i)

            max_count = 0
            for src in component:
                length = longest_path(src)
                if length == -1:
                    return -1
                max_count = max(max_count, length)
            result += max_count

        return result
