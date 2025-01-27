class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = defaultdict(list)
        for prereq, course in prerequisites:
            adj[course].append(prereq)
        
        def dfs(course):
            if course not in prereq_map:
                prereq_map[course] = set()
                for prereq in adj[course]:
                    prereq_map[course] |= dfs(prereq) # union

                prereq_map[course].add(course)

            return prereq_map[course]

        prereq_map = {} # map course -> hashset of indirect prereqs
        for course in range(numCourses):
            dfs(course)

        result = []
        for u, v in queries:
            result.append(u in prereq_map[v])
        
        return result
        
