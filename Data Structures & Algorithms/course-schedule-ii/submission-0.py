class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        pre_map = defaultdict(list)
        visited, visiting = set(),set()
        course = []

        for crs,pre in prerequisites:
            pre_map[crs].append(pre)
        
        def dfs(crs):
            if crs in visiting:
                return False
            
            if crs in visited:
                return True
            
            visiting.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            course.append(crs)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return course
        